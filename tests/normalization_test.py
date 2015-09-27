import unittest
from src.normalization import Normalization


class NormalizationTest(unittest.TestCase):

    def setUp(self):
        self.relative_url = '/path'
        self.pre_normalized_url = 'HTTP://www.Url.com:80/ab%c1/ef gh/ijk'
        self.normalized_url = 'http://www.url.com/ab%C1/ef%20gh/ijk'
        self.visited_links = ['/testpath', 'http://www.url.com', '/anotherpath',
                              'http://www.anotherurl.com', '/thirdpath']

    def normalization_test(self):
        normalized_url = Normalization(self.pre_normalized_url).validate()
        self.assertEqual(self.normalized_url, normalized_url)

    def relative_url_test(self):
        base_url_function = Normalization.get_url(self.relative_url, self.visited_links)
        self.assertEqual(self.visited_links[3] + self.relative_url, base_url_function)

    def non_relative_url_test(self):
        base_url_function = Normalization.get_url(self.visited_links[1], self.visited_links)
        self.assertEqual(self.visited_links[1], base_url_function)

if __name__ == '__main__':
    unittest.main()