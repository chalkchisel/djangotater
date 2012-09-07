import os
from django.db import models


class Version(models.Model):
    name = models.CharField(max_length=100)
    identifier = models.CharField(max_length=100)


class SourceFile(models.Model):
    version = models.ForeignKey(Version)
    path = models.CharField(max_length=5000)

    body = models.TextField()
    rendered = models.TextField(blank=True)

    @property
    def file_name(self):
        return os.path.split(self.path)[1]
