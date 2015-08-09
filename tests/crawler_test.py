from __future__ import print_function
import unittest
import sys

from src.crawler import Crawler


class CrawlerTest(unittest.TestCase):
    def crawl_test(self):
        sys.argv[1] = 'http://www.overstock.com'
        h = Crawler()
        self.assertTrue(len(h.extract_links()) > 0)

if __name__ == '__main__':
    unittest.main()
