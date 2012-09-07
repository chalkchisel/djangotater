import os
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Version(models.Model):
    name = models.CharField(max_length=100)
    identifier = models.CharField(max_length=100)


class SourceFile(MPTTModel):
    version = models.ForeignKey(Version)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

    path = models.CharField(max_length=5000)

    body = models.TextField()
    rendered = models.TextField(blank=True)

    @property
    def file_name(self):
        return os.path.split(self.path)[1]
