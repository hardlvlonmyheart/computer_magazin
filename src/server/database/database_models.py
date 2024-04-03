from peewee import *
import peewee
import settings

db = peewee.SqliteDatabase(database=f'{settings.DATABASE_PATH}/{settings.DATABASE_NAME}')

class BaseModel(Model):
    class Meta:
        database = db

class Client(BaseModel):
    full_name = CharField(max_length=45, default='')
    phone_number = CharField(default='')
    email = CharField(max_length=45, default='')

class Manager(BaseModel):
    full_name = CharField(max_length=45, default='')
    phone_number = CharField(default='')

class Storekeeper(BaseModel):
    full_name = CharField(max_length=45, default='')
    phone_number = CharField(default='')

class Order(BaseModel):
    id_client = ForeignKeyField(Client, default=0)
    id_master = ForeignKeyField(Manager, default=0)
    description = CharField(max_length=100, default='')
    price = CharField(max_length=45, default='')
    state_order = CharField(max_length=45, default='')
    review = CharField(max_length=1000, default='')

class Report(BaseModel):
    id_order = ForeignKeyField(Order, default=0)
    state = CharField(max_length=1000, default='')
    review = CharField(max_length=1000, default='')

class Supply(BaseModel):
    id_storekeeper = ForeignKeyField(Storekeeper, default=0)
    name = CharField(max_length=45, default='')
    quantity = IntegerField(default=0)
    date = CharField(default='')

class Master(BaseModel):
    full_name = CharField(max_length=45, default='')
    phone_number = CharField(default='')

class Details(BaseModel):
    name = CharField(max_length=45, default='')
    quantity = IntegerField(default=0)

class Post(BaseModel):
    post = CharField(max_length=255, default='')
    power_level = IntegerField(default=0)

class User(BaseModel):
    position = ForeignKeyField(Post, default=0)
    login = CharField(max_length=255, default='')
    password = CharField(max_length=255, default='')


db.create_tables([Client, Manager, Storekeeper, Order, Report, Supply, Master, Details, Post, User])