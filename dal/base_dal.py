from peewee import PostgresqlDatabase

from utils.config import Config


class BaseDal:
    @staticmethod
    def connect():
        return PostgresqlDatabase(database=Config.DB_BASE,
                                  user=Config.DB_USER, password=Config.DB_PASS,
                                  host=Config.DB_HOST, port=Config.DB_PORT)

    @staticmethod
    def schema():
        return Config.DB_SCHEMA
