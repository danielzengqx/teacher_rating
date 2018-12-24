from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
# Create your models here.
@python_2_unicode_compatible  # only if you need to support Python 2
class Comment(models.Model):
    content = models.CharField(max_length=5000)
    author = models.CharField(max_length=30)
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.content) + ' ' + str(self.author)

    class Meta:
        ordering = ('content', 'author', "time",)
