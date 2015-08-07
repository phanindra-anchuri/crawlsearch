__author__ = 'panchuri'

import unittest

from src.crawler import Hello


class MyTestCase(unittest.TestCase):
    def hello_test(self):
        h = Hello()
        self.assertEqual('Hello World', h.sayHello())


if __name__ == '__main__':
    unittest.main()
