# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'SourceFile.file_name'
        db.add_column('source_sourcefile', 'file_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=5000),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'SourceFile.file_name'
        db.delete_column('source_sourcefile', 'file_name')


    models = {
        'source.sourcefile': {
            'Meta': {'object_name': 'SourceFile'},
            'body': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'file_name': ('django.db.models.fields.CharField', [], {'max_length': '5000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '5000'}),
            'rendered': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'version': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['source.Version']"})
        },
        'source.version': {
            'Meta': {'object_name': 'Version'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['source']