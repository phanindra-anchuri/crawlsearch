from __future__ import print_function
import unittest

from src.crawler import Crawler


class CrawlerTest(unittest.TestCase):

    def crawl_test(self):
        h = Crawler('http://www.google.com')
        self.assertTrue(len(h.extract_links()) > 0)

    def robots_test(self):
        h = Crawler('http://www.google.com')
        self.assertTrue('path/catalogs' or 'http://www.google.com/catalogs' not in h.extract_links())

if __name__ == '__main__':
    unittest.main()
