import pymysql
import contextlib
@contextlib.contextmanager
def mysql():
  conn = pymysql.connect(host='localhost', port=3306, user='root',password='123456',db='yellow_sql', charset='utf8')
  cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
  try:
    yield cursor
  finally:
    conn.commit()
    cursor.close()
    conn.close()

class mysqlhelper:
    def query(self,sql):
        with mysql() as cursor:
            print(cursor.execute(sql))

    def get(self,sql):
        with mysql() as cursor:
            print(cursor.execute(sql))
            print(cursor.fetchall())
    def insert(self,sql):
        with mysql() as cursor:
            cursor.execute(sql)

