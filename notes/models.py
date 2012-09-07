from django.db import models
from source.models import SourceFile


class Note(models.Model):
    source_file = models.ForeignKey(SourceFile)
    body = models.TextField()
    start_line = models.PositiveIntegerField()
    end_line = models.PositiveIntegerField()
