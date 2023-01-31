import configparser
import pymysql

class Config():
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('bin/db_config.ini')
        self.connection = None
        self.host = self.config['database']['host']
        self.user = self.config['database']['user']
        self.password = self.config['database']['password']
        self.db = self.config['database']['db']

    def get_config(self):
        """
        Vrací konfiguraci databáze
        :return: host, user, password, db
        """
        return self.host, self.user, self.password, self.db

    def get_connection(self):
        """
        Vrací spojení s databází
        :return: připojení
        """
        self.connection = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            db=self.db
        )
        return self.connection

    def close_connection(self):
        """
        Uzavře spojení s databází
        :return: uzavřené spojení
        """
        return self.connection.close()

    