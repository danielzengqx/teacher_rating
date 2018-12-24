from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.

@python_2_unicode_compatible  # only if you need to support Python 2
class User(models.Model):
    name = models.CharField(max_length=200)
    passwd = models.CharField(max_length=200)
    u_id = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name


