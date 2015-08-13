import unittest

from src.persistence import Persister


class PersisterTest(unittest.TestCase):
    def persistence_test(self):
        persister = Persister()
        persister.save_url('www.google.com')
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
