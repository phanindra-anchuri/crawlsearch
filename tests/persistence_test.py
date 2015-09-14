import unittest
from src.persistence import Persister
from src.crawler import Crawler


class PersisterTest(unittest.TestCase):

    def persistence_test(self):
        persister = Persister()
        persister.save_url('www.google.com')
        self.assertTrue(True)

    def get_urls_test(self):
        url = 'www.facebook.com'
        Crawler(url, 1).crawl_links()
        results = Persister().get_urls()
        self.assertTrue(len(results) >= 1)

    def tearDown(self):
        conn = Persister().connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM crawl_results")
        conn.close()

if __name__ == '__main__':
    unittest.main()
