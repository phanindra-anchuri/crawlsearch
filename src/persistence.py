import sqlite3


class Persister:

    def __init__(self):
        pass

    @staticmethod
    def connection():
        conn = sqlite3.connect('crawl.db')
        conn.execute('''CREATE TABLE if not exists crawl_results
                 (date text, url text)''')
        return conn

    def save_url(self, url):
        conn = self.connection()
        try:
            insert = "INSERT INTO crawl_results VALUES (CURRENT_TIMESTAMP, '"
            insert += url + "')"
            conn.execute(insert)
        except sqlite3.Error as e:
            print e.message

            if conn is not None:
                conn.rollback()
        finally:
            conn.commit()
            conn.close()

    def get_urls(self):
        conn = self.connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT url FROM crawl_results")
            results = [cursor.fetchall()]
            return results

        finally:
            conn.close()