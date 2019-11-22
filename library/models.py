from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name

# {
#     "user": {
#        "name": "Дмитрий",
#        "email": "dima@mail.ru"
#     }
# }


class Book(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()

    def __str__(self):
        return self.title

# {
#     "book": {
#        "title": "Foo",
#        "description": "Bla"
#     }
# }


class Assignment(models.Model):
    user = models.ForeignKey('User', related_name='Assignments', on_delete=models.CASCADE)
    book = models.ForeignKey('Book', related_name='Assignments', on_delete=models.CASCADE)
    fullname = '{} - {}'.format(user, book)

    def __str__(self):
        return self.fullname


