import unittest
from urllib2 import URLError
from src.crawler import Crawler
from src.persistence import Persister


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

    def crawled_links_test(self):
        url = 'http://www.google.com'
        duplicate_url = 'http://www.google.com/intl/en/options/'
        Crawler(url, 5).crawl_links()
        self.assertTrue(Persister().get_urls().count(duplicate_url) <= 1)
        self.assertFalse(Persister().get_urls().count(duplicate_url) > 1)

    def tearDown(self):
        conn = Persister().connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM crawl_results")
        conn.close()

if __name__ == '__main__':
    unittest.main()