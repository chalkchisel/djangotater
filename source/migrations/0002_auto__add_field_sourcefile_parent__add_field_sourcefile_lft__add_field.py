# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'SourceFile.parent'
        db.add_column('source_sourcefile', 'parent',
                      self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['source.SourceFile']),
                      keep_default=False)

        # Adding field 'SourceFile.lft'
        db.add_column('source_sourcefile', 'lft',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0, db_index=True),
                      keep_default=False)

        # Adding field 'SourceFile.rght'
        db.add_column('source_sourcefile', 'rght',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0, db_index=True),
                      keep_default=False)

        # Adding field 'SourceFile.tree_id'
        db.add_column('source_sourcefile', 'tree_id',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0, db_index=True),
                      keep_default=False)

        # Adding field 'SourceFile.level'
        db.add_column('source_sourcefile', 'level',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0, db_index=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'SourceFile.parent'
        db.delete_column('source_sourcefile', 'parent_id')

        # Deleting field 'SourceFile.lft'
        db.delete_column('source_sourcefile', 'lft')

        # Deleting field 'SourceFile.rght'
        db.delete_column('source_sourcefile', 'rght')

        # Deleting field 'SourceFile.tree_id'
        db.delete_column('source_sourcefile', 'tree_id')

        # Deleting field 'SourceFile.level'
        db.delete_column('source_sourcefile', 'level')


    models = {
        'source.sourcefile': {
            'Meta': {'object_name': 'SourceFile'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['source.SourceFile']"}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '5000'}),
            'rendered': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
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