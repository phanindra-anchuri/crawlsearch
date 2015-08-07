__author__ = 'panchuri'

import unittest

from src.crawler import Hello


class CrawlerTest(unittest.TestCase):
    def hello_test(self):
        h = Hello()
        self.assertTrue('Google' in h.say_hello())


if __name__ == '__main__':
    unittest.main()
