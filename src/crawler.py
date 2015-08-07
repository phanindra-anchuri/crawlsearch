__author__ = 'panchuri'

from bs4 import BeautifulSoup
import urllib2


class Crawler:

    @staticmethod
    def crawl():
        url = 'http://www.google.com'
        page = urllib2.urlopen(url)
        soup = BeautifulSoup(page.read())
        return soup.title

    def __init__(self):
        pass
