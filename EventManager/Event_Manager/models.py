from django.db import models
import datetime
from django.utils.timezone import make_aware

# Create your models here.
class Events(models.Model):
    name = models.CharField(max_length=30, unique=True)
    desciption = models.TextField()
    poster_link = models.URLField()
    from_dt = models.DateTimeField()
    to_dt = models.DateTimeField()
    deadline = models.DateTimeField()
    email = models.EmailField()
    password = models.CharField(max_length=40)

    def _str_(self):
        return self.name
