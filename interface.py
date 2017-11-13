from os import path

import psycopg2

DBNAME = 'news'
DB_VIEWS = path.normpath('/vagrant/news/views.sql')


class Interface:
    def __init__(self, dbname=DBNAME):
        self._dbname = dbname
        self._conn = psycopg2.connect(database=self._dbname)
        self._init_db_views()

    def _init_db_views(self):
        """Execute PSQL views file"""
        with self._conn:
            with self._conn.cursor() as curs:
                with open(DB_VIEWS, 'r') as f:
                    curs.execute(f.read())
                    self._conn.commit()

    def execute_query(self, query):
        """Executes a PSQL query"""
        self._conn.set_session(readonly=True)

        with self._conn:
            with self._conn.cursor() as curs:
                curs.execute(query)

                r = {'status': curs.statusmessage,
                     'text': curs.fetchall(),
                     'query': curs.query,
                     'headers': [desc[0] for desc in curs.description]}

        self._conn.set_session(readonly=None)

        return r

    def close(self):
        """Close DB connection"""
        self._conn.close()
