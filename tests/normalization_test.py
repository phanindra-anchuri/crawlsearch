import unittest
from src.normalization import Normalization


class NormalizationTest(unittest.TestCase):

    """
    Tests ran before converting these functions to "private."

    def scheme_test(self):
        uppercase_scheme = 'HTTP://www.url.com'
        relative = "/something/"
        n = Normalization(relative).scheme()
        self.assertEqual(n, 'http://www.url.com')

    def netloc_test(self):
        uppercase_netloc = 'http://www.URL.com'
        n = Normalization(uppercase_netloc).netloc()
        self.assertEqual(n, 'http://www.url.com')

    def escape_sequence_test(self):
        escape_url = 'HTTP://www.Url.com/a%c2%b1b'
        n = Normalization(escape_url).escape_sequence()
        self.assertEqual(n, 'http://www.url.com/a%C2%B1b')

    def port_test(self):
        port_url = 'http://www.url.com:8080'
        n = Normalization(port_url).port()
        self.assertEqual(n, 'http://www.url.com')

    def decode_test(self):
        spaced_url = 'http://www.url.com/as bda/dba'
        n = Normalization(spaced_url).spaces()
        self.assertEqual(n, 'http://www.url.com/as%20bda/dba')

        """

    def normalization_test(self):
        url = 'HTTP://www.Url.com:80/ab%c1/ef gh/ijk'
        n = Normalization(url).get_url()
        self.assertEqual(n, 'http://www.url.com/ab%C1/ef%20gh/ijk')

if __name__ == '__main__':
    unittest.main()