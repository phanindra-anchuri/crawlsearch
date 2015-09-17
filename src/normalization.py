# TODO Need to find a way to append paths to base url for relative urls

import re
from urlparse import urlparse
from urllib2 import quote


class Normalization:

    def __init__(self, url):
        self.url = url

    def get_url(self):
        return Normalization(self.url).__escape_sequence()

    def __scheme(self):
        parsed_url = urlparse(self.url)
        if parsed_url.scheme == '':
            new_scheme = parsed_url._replace(scheme='http://', netloc=parsed_url.path, path= '')
            return new_scheme.geturl()
        replaced_scheme = parsed_url._replace(scheme=parsed_url.scheme.lower())
        new_url = replaced_scheme.geturl()
        return new_url

    def __netloc(self):
        url = urlparse(self.__scheme())
        replaced_netloc = url._replace(netloc=url.netloc.lower())
        new_url = replaced_netloc.geturl()
        return new_url

    def __port(self):
        url = urlparse(self.__netloc())
        netloc_split = url._replace(netloc="{}{}".format(url.hostname, ''))
        new_url = netloc_split.geturl()
        return new_url

    def __spaces(self):
        url = urlparse(self.__port())
        decoded_path = quote(url.path, safe='%/@')
        decoded_url = url._replace(path=decoded_path)
        new_url = decoded_url.geturl()
        return new_url

    def __escape_sequence(self):
        url = urlparse(self.__spaces())
        escape_regex = r'(%[a0-z9]{2})'
        escape_match = re.search(escape_regex, url.path)
        if escape_match:
            escape_upper = re.sub(escape_regex, lambda e: e.group(0).upper(), url.path)
            replaced_escape = url._replace(path=escape_upper)
            new_url = replaced_escape.geturl()
            return new_url
        else:
            return url.geturl()