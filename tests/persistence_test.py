import unittest
from src.persistence import Persister


class PersisterTest(unittest.TestCase):

    def setUp(self):
        self.persister = Persister()
        self.url = 'http://www.url.com'

    def persistence_test(self):
        self.assertEqual(self.persister.save_url(self.url), None)

    def get_urls_test(self):
        self.persister.save_url(self.url)
        self.persister.save_url(self.url)
        self.assertTrue(self.persister.get_urls() > 1)

    def tearDown(self):
        conn = self.persister.connection()
        conn.execute("DELETE FROM crawl_results")
        conn.commit()

if __name__ == '__main__':
    unittest.main()