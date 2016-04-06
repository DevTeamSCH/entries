from django.db import models
from django.contrib.auth.models import User

class Entry(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(blank=True)
    url = models.URLField(blank=True)
    logo = models.ImageField(blank=True)
    added_by = models.ForeignKey(User)

    def __str__(self):
        return self.title
