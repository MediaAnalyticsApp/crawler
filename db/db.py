import pymysql.cursors
from conf import config


class Db:
    def __init__(self):
        pass

    @staticmethod
    def connect():
        cfg = config.CrawlerConfig()
        db_host = cfg.get_db_host()
        db_name = cfg.get_db_name()
        db_user = cfg.get_db_user()
        db_pass = cfg.get_db_password()

        connection = pymysql.connect(host=db_host,
                                     user=db_user,
                                     password=db_pass,
                                     db=db_name,
                                     cursorclass=pymysql.cursors.DictCursor)

        return connection

    def get_all_persons(self):
        sql = "SELECT * FROM persons"
        try:
            cursor = self.connect().cursor()
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        finally:
            self.connect().close()
