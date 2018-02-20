import pymysql.cursors
from conf import config


class CrawlerDb:
    def __init__(self):
        self.cfg = config.CrawlerConfig()

    def connect(self):
        db_host = self.cfg.get_db_host()
        db_name = self.cfg.get_db_name()
        db_user = self.cfg.get_db_user()
        db_pass = self.cfg.get_db_password()

        connection = pymysql.connect(host=db_host,
                                     user=db_user,
                                     password=db_pass,
                                     db=db_name,
                                     cursorclass=pymysql.cursors.DictCursor,
                                     autocommit=True)

        return connection

    def get_all_persons(self):
        sql = "SELECT * FROM `persons`"
        try:
            cursor = self.connect().cursor()
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        finally:
            self.connect().close()

    def get_sites(self):
        sql = "SELECT * FROM `sites`"
        try:
            cursor = self.connect().cursor()
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        finally:
            self.connect().close()

    def add_pages(self, site_id, pages):
        sql = "INSERT INTO `pages` (`url`, `site_id`) VALUES (%s, %s)"
        n = 0
        for page in pages:
            if n < 10:
                try:
                    cursor = self.connect().cursor()
                    cursor.execute(sql, (page, site_id))
                    self.connect().commit()
                except pymysql.err.IntegrityError:
                    pass
                finally:
                    self.connect().close()
                n += 1
