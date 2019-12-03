# Generated by Django 2.2.7 on 2019-12-02 11:36

from django.db import migrations
import random, string, uuid

from random import randint


def randomString(x):
    lett = 'ab1cd2ef3gh4ij5kl6mn7op8qr9stuvwxyz'
    return ''.join([random.choice(lett) for i in range(x)])


def add(apps, schema_editor):
    User = apps.get_model('library', 'User')
    Book = apps.get_model('library', 'Book')
    Assignment = apps.get_model('library', 'Assignment')

    db_alias = schema_editor.connection.alias
    for x in range(1, 11):

        User.objects.using(db_alias).create([
            User(name='{0}'.format(randomString(x)), email='{0}@mail.ru'.format(randomString(x))),
        ])

        Book.objects.using(db_alias).create([
            Book(title='{0}'.format(randomString(x)),
                 description='Описание книги под номером {0}'.format(randomString(x))),
        ])

        users = random.choice(User.objects.all())
        books = random.choice(Book.objects.all())

        Assignment.objects.using(db_alias).create([
            Assignment(user=users, book=books)
        ])


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20191202_1136'),
    ]

    operations = [
        migrations.RunPython(add, reverse_code=migrations.RunPython.noop),
    ]

