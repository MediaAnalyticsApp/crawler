import configparser
import os


class CrawlerConfig:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.optionxform = str
        path_cfg = str(os.path.dirname(os.path.abspath(__file__)))
        self.config_file = path_cfg + '/config.ini'
        if os.path.exists(self.config_file):
            try:
                self.config.read(self.config_file)
            except configparser.ParsingError:
                print('Config config.ini syntax error')
                exit()
        elif not os.path.exists(self.config_file):
            self.config.add_section('DataBase')
            self.config.set('DataBase', 'host', 'localhost')
            self.config.set('DataBase', 'port', '3306')
            self.config.set('DataBase', 'name', 'traineeship')
            self.config.set('DataBase', 'user', 'traineeship')
            self.config.set('DataBase', 'password', 'db_password')
            self.config.add_section('Log')
            self.config.set('Log', 'logwrite', '1')
            self.config.set('Log', 'logname', 'crawler.log')
            with open(self.config_file, 'w') as configfile:
                self.config.write(configfile)

    def get_db_host(self):
        try:
            host = self.config.get('DataBase', 'host')
        except (configparser.NoOptionError, configparser.NoSectionError):
            print('Error section DataBase or option host in config file')
            host = 'localhost'
        return host

    def get_db_port(self):
        try:
            port = self.config.get('DataBase', 'port')
        except (configparser.NoOptionError, configparser.NoSectionError):
            print('Error section DataBase or option port in config file')
            port = '3306'
        return port

    def get_db_name(self):
        try:
            name = self.config.get('DataBase', 'name')
        except (configparser.NoOptionError, configparser.NoSectionError):
            print('Error section DataBase or option name in config file')
            name = 'db_name'
        return name

    def get_db_user(self):
        try:
            user = self.config.get('DataBase', 'user')
        except (configparser.NoOptionError, configparser.NoSectionError):
            print('Error section DataBase or option user in config file')
            user = 'db_user'
        return user

    def get_db_password(self):
        try:
            password = self.config.get('DataBase', 'password')
        except (configparser.NoOptionError, configparser.NoSectionError):
            print('Error section DataBase or option password in config file')
            password = 'db_pass'
        return password

    def get_logwrite(self):
        try:
            log = self.config.getboolean('Log', 'logwrite')
        except (configparser.NoOptionError, configparser.NoSectionError):
            print('Error section Log or option logwrite in config file')
            log = True
            exit()
        return log

    def get_logname(self):
        try:
            log_path = self.config.get('Log', 'logname')
        except (configparser.NoOptionError, configparser.NoSectionError):
            print('Error section Log or option logname in config file')
            log_path = 'crawler.log'
            exit()
        return log_path
