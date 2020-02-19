#!/bin/python3

import unittest
import datetime
import logging
import sys
import os

from sitemap import SiteMap


class TestSiteMap(unittest.TestCase):
    """Test SiteMap class.

    TODO: Mock requests instead of polling example.org"""

    @classmethod
    def setUpClass(cls):
        logging.info("Setting up tests.")
        cls.test_output_file = "test_sitemap.txt"
        cls.test_url = "https://example.org"
        cls.sitemap = SiteMap(cls.test_url, worker_timeout=6)

    @classmethod
    def tearDownClass(cls):
        logging.info("Cleaning up after tests.")
        os.remove(cls.test_output_file)

    def test_add(self):
        self.sitemap.add(self.test_url)
        self.sitemap.add(self.test_url)
        self.sitemap.add(self.test_url)
        self.assertTrue(self.sitemap)
        self.assertEqual(len(self.sitemap), 1)

    def test_contains(self):
        self.sitemap.add(self.test_url)
        self.assertTrue(self.sitemap)
        self.assertTrue(self.test_url in self.sitemap)

    def test_pop(self):
        self.sitemap.add(self.test_url)
        popped = self.sitemap.pop()
        self.assertEqual(popped, self.test_url)
        self.assertEqual(len(self.sitemap), 0)

    def test_dump_to_file(self):
        self.sitemap.dump_to_file(self.test_output_file)

        with open(self.test_output_file) as f:
            line = f.readline()

        self.assertEqual(line, f'{self.test_url}\n')

    def test_scrape(self):
        self.sitemap()
        self.assertTrue(self.sitemap)
        self.assertEqual(len(self.sitemap), 1)
        self.assertTrue(self.test_url in self.sitemap)
        self.assertFalse(
            "https://www.iana.org/domains/example" in self.sitemap)

    def test_scrape_performance(self):
        """TODO: Use timeit library or a time-counting decorator, mock requests to reduce network I/O."""

        start_time = datetime.datetime.now()
        self.sitemap()
        elapsed_time = datetime.datetime.now()
        difference = elapsed_time - start_time - \
            datetime.timedelta(seconds=self.sitemap.worker_timeout)

        self.assertLessEqual(datetime.timedelta(
            seconds=difference.seconds, microseconds=difference.microseconds), datetime.timedelta(seconds=3))


if __name__ == "__main__":
    logging.basicConfig(stream=sys.stderr)
    logging.getLogger("sitemap").setLevel(logging.DEBUG)

    unittest.main()
