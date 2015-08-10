from __future__ import print_function
import unittest

from src.crawler import Crawler


class CrawlerTest(unittest.TestCase):

    def crawl_test(self):
        h = Crawler('http://www.overstock.com')
        self.assertTrue(len(h.extract_links()) > 0)

if __name__ == '__main__':
    unittest.main()
