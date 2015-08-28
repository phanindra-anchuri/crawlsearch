# from __future__ import print_function
import sys
import urllib2
from reppy.cache import RobotsCache
from urlparse import urlparse

from bs4 import BeautifulSoup


class Crawler:

    def extract_links(self):

        page = urllib2.urlopen(self.base_url)
        robots = RobotsCache()
        x = robots.fetch(self.base_url)
        soup = BeautifulSoup(page.read(), 'html.parser')
        atags = soup.find_all('a')
        links = [urlparse(str(atag.get('href'))) for atag in atags]
        allowed_links = [str(link) for link in links if x.allowed(link, 'crawler')]
        # print '\n'.join(str(link) for link in allowed_links)
        return allowed_links

    def __init__(self, url):
        self.base_url = url

if __name__ == '__main__':
    crawler = Crawler(sys.argv[1])
    crawler.extract_links()
