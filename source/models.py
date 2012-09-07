import os
from django.db import models


class Version(models.Model):
    name = models.CharField(max_length=100)
    identifier = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class SourceFile(models.Model):
    version = models.ForeignKey(Version)

    path = models.CharField(max_length=5000)
    file_name = models.CharField(max_length=5000)

    body = models.TextField(blank=True)
    rendered = models.TextField(blank=True)

    def __unicode__(self):
        return self.file_name

    @property
    def file_name(self):
        return os.path.split(self.path)[1]
