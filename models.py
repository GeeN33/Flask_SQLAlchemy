from peewee import *

db = SqliteDatabase('Sqlite_db')

class BaseModel(Model):
    class Meta:
        database = db

class Category(BaseModel):
    class Meta:
        db_table = 'category'
    name = CharField(max_length=50)

class News(BaseModel):
    class Meta:
        db_table = 'news'

    name = CharField(max_length=50)
    text = CharField(max_length=200)
    category_id = ForeignKeyField(Category)

#db.create_tables([Category,News])