# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'SourceFile.rght'
        db.delete_column('source_sourcefile', 'rght')

        # Deleting field 'SourceFile.parent'
        db.delete_column('source_sourcefile', 'parent_id')

        # Deleting field 'SourceFile.lft'
        db.delete_column('source_sourcefile', 'lft')

        # Deleting field 'SourceFile.level'
        db.delete_column('source_sourcefile', 'level')

        # Deleting field 'SourceFile.tree_id'
        db.delete_column('source_sourcefile', 'tree_id')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'SourceFile.rght'
        raise RuntimeError("Cannot reverse this migration. 'SourceFile.rght' and its values cannot be restored.")
        # Adding field 'SourceFile.parent'
        db.add_column('source_sourcefile', 'parent',
                      self.gf('mptt.fields.TreeForeignKey')(related_name='children', null=True, to=orm['source.SourceFile'], blank=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'SourceFile.lft'
        raise RuntimeError("Cannot reverse this migration. 'SourceFile.lft' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'SourceFile.level'
        raise RuntimeError("Cannot reverse this migration. 'SourceFile.level' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'SourceFile.tree_id'
        raise RuntimeError("Cannot reverse this migration. 'SourceFile.tree_id' and its values cannot be restored.")

    models = {
        'source.sourcefile': {
            'Meta': {'object_name': 'SourceFile'},
            'body': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
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