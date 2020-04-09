from peewee import *

database = SqliteDatabase('icd10merge.db')

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Txtcodes(BaseModel):
    code = TextField(null=True)
    long_desc = TextField(null=True)
    short_desc = TextField(null=True)

    class Meta:
        table_name = 'txtcodes'
        primary_key = False

class Xmlcodes(BaseModel):
    code = TextField(null=True)
    diag_name = TextField(null=True)
    ext_char = TextField(null=True)
    ext_desc = TextField(null=True)
    subcatid = TextField(null=True)

    class Meta:
        table_name = 'xmlcodes'
        primary_key = False

class Xmlsubcats(BaseModel):
    category = TextField(null=True)
    first = TextField(null=True)
    id = TextField(null=True)
    last = TextField(null=True)
    subcat = TextField(null=True)

    class Meta:
        table_name = 'xmlsubcats'
        primary_key = False
