# from __future__ import print_function
import sys
import urllib2
from urllib2 import HTTPError, URLError
from collections import deque
from reppy.cache import RobotsCache

from bs4 import BeautifulSoup


class Crawler:

    @staticmethod
    def extract_links(url):
        page = urllib2.urlopen(url)
        robots = RobotsCache()
        x = robots.fetch(url)
        soup = BeautifulSoup(page.read(), 'html.parser')
        atags = soup.find_all('a')
        links = [str(atag.get('href')) for atag in atags]
        allowed_links = [str(link) for link in links if x.allowed(link, 'crawler')]
        # print '\n'.join(str(link) for link in allowed_links)
        return allowed_links

    def crawl_links(self):
        depth = 0
        queue = deque()
        queue.appendleft(self.base_url)
        while len(queue) > 0 and depth <= self.depth:
            url = queue.popleft()
            try:
                urls = [str(link) for link in self.extract_links(url)]
                if urls.count(url) > 1:
                    urls.remove(url)
            except (ValueError, HTTPError, URLError):
                continue
            depth += 1
            for url in urls:
                queue.append(str(url))

    def __init__(self, url, depth):
        self.base_url = url
        self.depth = depth

if __name__ == '__main__':
    crawler = Crawler(sys.argv[1], int(sys.argv[2]))
    crawler.crawl_links()

