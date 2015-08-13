__author__ = 'phanindra'

import sqlite3


class Persister:
    def __init__(self):
        pass

    def save_url(self, url):
        conn = sqlite3.connect('crawl.db')
        conn.execute('''CREATE TABLE if not exists crawl_results
             (date text, url text)''')
        insert = "INSERT INTO crawl_results VALUES ('2006-01-05', '"
        insert += url + "')"
        conn.execute(insert)
        conn.commit()
        conn.close()
