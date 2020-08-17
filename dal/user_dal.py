from peewee import PostgresqlDatabase, Model, IntegerField, CharField, DateTimeField

from dal.base_dal import BaseDal


class UserDal:

    @staticmethod
    def get_select():
        class User(Model):
            id = IntegerField(primary_key=True)
            email = CharField()
            created_at = DateTimeField()

            class Meta:
                database = BaseDal.connect()
                schema = BaseDal.schema()
                table_name = 'user'

        try:
            users = User.select()
        except User.DoesNotExist:
            users = None
        finally:
            return users
