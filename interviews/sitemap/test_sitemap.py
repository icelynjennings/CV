#!/bin/python3

import unittest
import datetime
import logging
import sys
import os

from sitemap import SiteMap
import requests

logging.basicConfig()
logger = logging.getLogger("test_sitemap")
logger.setLevel(logging.DEBUG)


class TestSiteMap(unittest.TestCase):
    """Test SiteMap class.

    TODO: Mock requests instead of polling example.org"""

    @classmethod
    def setUpClass(cls):
        logger.debug("Setting up tests.")
        cls.test_output_file = "test_sitemap.txt"
        cls.test_url = "https://example.org"
        cls.sitemap = SiteMap(cls.test_url, worker_timeout=6)

    @classmethod
    def tearDownClass(cls):
        logger.debug("Cleaning up after tests.")
        os.remove(cls.test_output_file)

    def test_add(self):
        self.sitemap.add(self.test_url)
        self.sitemap.add(self.test_url)
        self.sitemap.add(self.test_url)
        self.assertTrue(self.sitemap)
        self.assertEqual(len(self.sitemap), 1)

    def test___contains__(self):
        self.sitemap.add(self.test_url)
        self.assertTrue(self.sitemap)
        self.assertIn(self.test_url, self.sitemap)

    def test_pop(self):
        self.sitemap.add(self.test_url)
        popped = self.sitemap.pop()
        self.assertEqual(popped, self.test_url)
        self.assertEqual(len(self.sitemap), 0)

    def test_request(self):
        r = self.sitemap.request("https://google.com")
        self.assertEqual(r.status_code, 200)
        self.assertIn("google.com", r.text)
        self.assertRaises(requests.exceptions.RequestException,
                          self.sitemap.request("fake://fake.fake"))

    def test_dump_to_file(self):
        self.sitemap.dump_to_file(self.test_output_file)
        with open(self.test_output_file) as f:
            line = f.readline()
        self.assertEqual(line, f'{self.test_url}\n')

    def test___call__(self):
        """TODO: Use timeit library or a time-counting decorator, mock requests to reduce network I/O."""
        start_time = datetime.datetime.now()
        self.sitemap()
        execution_time = datetime.datetime.now() - start_time - \
            datetime.timedelta(seconds=self.sitemap.worker_timeout)
        self.assertLessEqual(datetime.timedelta(
            seconds=execution_time.seconds, microseconds=execution_time.microseconds), datetime.timedelta(seconds=3))

        self.assertTrue(self.sitemap)
        self.assertEqual(len(self.sitemap), 1)
        self.assertIn(self.test_url, self.sitemap)
        self.assertNotIn(
            "https://www.iana.org/domains/example", self.sitemap)


if __name__ == "__main__":

    unittest.main()
