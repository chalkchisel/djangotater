# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Version'
        db.create_table('source_version', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('identifier', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('source', ['Version'])

        # Adding model 'SourceFile'
        db.create_table('source_sourcefile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('version', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['source.Version'])),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=5000)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('rendered', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('source', ['SourceFile'])


    def backwards(self, orm):
        # Deleting model 'Version'
        db.delete_table('source_version')

        # Deleting model 'SourceFile'
        db.delete_table('source_sourcefile')


    models = {
        'source.sourcefile': {
            'Meta': {'object_name': 'SourceFile'},
            'body': ('django.db.models.fields.TextField', [], {}),
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