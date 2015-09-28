import unittest
from src.crawler import Crawler


class CrawlerTest(unittest.TestCase):

    def setUp(self):
        self.test_url = 'http://www.google.com'
        self.invalid_url = 'invalid_url:'
        self.robot_path = 'path/catalogs'
        self.robot_url = 'http://www.google.com/catalogs'

    def extract_test(self):
        crawler = Crawler(self.test_url, 1)
        extracted_urls = crawler.extract_links(self.test_url)
        self.assertTrue(len(extracted_urls) > 0)

    def robots_test(self):
        crawler = Crawler(self.test_url, 1)
        self.assertTrue(self.robot_path and self.robot_url
                        not in crawler.extract_links(self.test_url))

if __name__ == '__main__':
    unittest.main()