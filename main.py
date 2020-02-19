#!/bin/python3

import sys
import logging
import datetime
import timeit

from sitemap import SiteMap


def run(url="https://example.com") -> SiteMap:
    sitemap = SiteMap(
        url=url,
        max_workers=30,
        worker_timeout=6
    )

    start_time = datetime.datetime.now()
    sitemap()
    end_time = datetime.datetime.now()

    difference = end_time - start_time - \
        datetime.timedelta(seconds=sitemap.worker_timeout)

    print(f"Scraped {len(sitemap)} url(s) into {sitemap} in {str(difference)}")
    sitemap.dump_to_file('sitemap.txt')
    print("Dumped to sitemap.txt")
    return sitemap


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr)

    logging_enabled = False
    if logging_enabled:
        logging.getLogger("sitemap").setLevel(logging.DEBUG)

    run()
