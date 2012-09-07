# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Note'
        db.create_table('notes_note', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('source_file', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['source.SourceFile'])),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('start_line', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('end_line', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('notes', ['Note'])


    def backwards(self, orm):
        # Deleting model 'Note'
        db.delete_table('notes_note')


    models = {
        'notes.note': {
            'Meta': {'object_name': 'Note'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'end_line': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source_file': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['source.SourceFile']"}),
            'start_line': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
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

    complete_apps = ['notes']