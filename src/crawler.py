# from __future__ import print_function
import sys
import urllib2
from urlparse import urlparse

from bs4 import BeautifulSoup


class Crawler:

    def extract_links(self):
        page = urllib2.urlopen(self.base_url)
        soup = BeautifulSoup(page.read(), 'html.parser')
        atags = soup.find_all('a')
        links = [urlparse(str(atag.get('href'))) for atag in atags]
        print '\n'.join(str(link) for link in links)
        # print(type(links[0]))
        return links

    def __init__(self):
        self.base_url = sys.argv[1]

if __name__ == '__main__':
    crawler = Crawler()
    crawler.extract_links()
