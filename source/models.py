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

    @property
    def full_path(self):
        return os.path.join(self.path, self.file_name)

    def __unicode__(self):
        return self.full_path
