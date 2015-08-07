__author__ = 'panchuri'

import unittest

from src.crawler import Crawler


class CrawlerTest(unittest.TestCase):
    def crawl_test(self):
        h = Crawler()
        self.assertTrue('Google' in h.crawl())


if __name__ == '__main__':
    unittest.main()
