#!/bin/python3

import requests
import logging

from queue import Queue, Empty
from urllib.parse import urljoin, urlparse
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup

logger = logging.getLogger('sitemap')


class SiteMap(set):  # ;)
    """Implements a data structure for fetching and manipulating the sitemap of a given website."""

    def __init__(self, url, max_workers=30, worker_timeout=10):
        super(SiteMap, self).__init__()
        self.queue = Queue()
        self.pool = ThreadPoolExecutor(max_workers=max_workers)
        self.domain = self.strip_url(url)
        self.worker_timeout = worker_timeout
        self.failed_requests = set([])
        self.queue.put(self.domain)

    def __len__(self) -> int:
        return super(SiteMap, self).__len__()

    def __iter__(self) -> set:
        return (item for item in super().__iter__())

    def __repr__(self) -> str:
        return f"{super().__repr__()}"

    def __contains__(self, item) -> bool:
        return super(SiteMap, self).__contains__(item)

    def add(self, url) -> None:
        """Adds input URL to the set.
        TODO: Validate input is a URL."""
        super(SiteMap, self).add(url)

    def remove(self, url) -> None:
        """Removes input URL from set."""
        super(SiteMap, self).remove(url)

    def pop(self) -> str:
        """Pops a random URL from the set."""
        return super(SiteMap, self).pop()

    def strip_url(self, url) -> str:
        """Helper init function to get the scheme and apex of the url."""
        return f'{urlparse(url).scheme}://{urlparse(url).netloc}'

    def filter_internal_urls(self, urls) -> list:
        """Returns a clean list of URLs, internal to a desired domain only."""
        internal_urls = list(filter(lambda url: url.startswith(
            '/') or url.startswith(self.domain), urls))
        return [urljoin(self.domain, url) for url in internal_urls]

    def process_urls(self, response) -> None:
        """Callback function appending newfound links to the sitemap."""
        r = response.result()
        if r and r.status_code == 200:
            soup = BeautifulSoup(r.text, 'html.parser')
            all_urls = [a['href'] for a in soup.find_all('a', href=True)]
            valid_urls = self.filter_internal_urls(all_urls)
            for url in valid_urls:
                self.queue.put(url)

    def request(self, url) -> requests.Response:
        """Request a URL. Record failures in case we want to retry later."""
        logger.info(f"GET {url}")
        try:
            r = requests.get(url, timeout=7)
            return r
        except requests.RequestException as e:
            logger.debug(f"Exception {e} while retrieving {url}")
            self.failed_requests.add(url)
            return None

    def dump_to_file(self, filepath) -> None:
        """Serialize entries to file while freeing memory."""
        with open(filepath, 'w') as f:
            while self:
                f.write(f'{self.pop()}\n')

    def retry(self) -> None:
        """Re-enqueue URLs which failed to scrape."""
        raise NotImplementedError

    def drop_dead(self) -> None:
        """Drop dead links from the sitemap."""
        raise NotImplementedError

    def resync(self) -> None:
        """One-stop maintenance wrapper function for our dataset"""
        raise NotImplementedError

    def get_sitemap_xml(self) -> str:
        """Return a tree of the server's sitemap.xml"""
        raise NotImplementedError

    def __call__(self) -> None:
        while True:
            try:
                url = self.queue.get(timeout=self.worker_timeout)
                if url not in self:
                    self.add(url)
                    job = self.pool.submit(self.request, url)
                    job.add_done_callback(self.process_urls)
            except Empty:
                # Worker queue has been empty for {self.worker_timeout} seconds.
                self.add(self.domain)
                return  # End execution.
            except Exception as e:
                logger.debug(e)
                continue
