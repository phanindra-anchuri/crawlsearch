from __future__ import print_function
from urllib2 import URLError
import unittest

from src.crawler import Crawler


class CrawlerTest(unittest.TestCase):

    def extract_test(self):
        url = 'http://www.google.com'
        h = Crawler(url, 1)
        self.assertTrue(len(h.extract_links(url)) > 0)

    def robots_test(self):
        url = 'http://www.google.com'
        h = Crawler(url, 1)
        self.assertTrue('path/catalogs' and 'http://www.google.com/catalogs' not in h.extract_links(url))

    def crawl_test(self):
        url = 'invalidurl:'
        h = Crawler(url, 1)
        self.assertIsNone(h.crawl_links())
        self.assertRaises(URLError, h.crawl_links())

if __name__ == '__main__':
    unittest.main()
