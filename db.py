from peewee import *


DATABASE_NAME = "u2565799_default"
HOST = "31.31.196.115"
USER = "u2565799_default"
PASSWORD = "T20Qm0naCpMfA62p"
connection = MySQLDatabase(DATABASE_NAME, host=HOST,
                           port=3306, user=USER, password=PASSWORD)


class ModelBase(Model):
    class Meta:
        database = connection


class Event(ModelBase):
    name = TextField(null=False)
    link = TextField(null=False)
    description = TextField()
    date = DateField()


connection.connect()
# connection.create_tables([Event])


def add_event(Events):

    try:
        inBaseEvent = Event.get(Event.name == Events[0])
    except:
        inBaseEvent = False

    if not (inBaseEvent):
        event = Event.create(
            name=Events[0], date=Events[1]+' '+Events[4], link=Events[2], description=Events[3])
        event.save()
