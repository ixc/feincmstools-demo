# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Text.content'
        db.delete_column('meetups_meetup_text', 'content')

        # Adding field 'Text.text'
        db.add_column('meetups_meetup_text', 'text',
                      self.gf('markitup.fields.MarkupField')(default='', no_rendered_field=True, blank=True),
                      keep_default=False)

        # Adding field 'Text._text_rendered'
        db.add_column('meetups_meetup_text', '_text_rendered',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Text.content'
        db.add_column('meetups_meetup_text', 'content',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Deleting field 'Text.text'
        db.delete_column('meetups_meetup_text', 'text')

        # Deleting field 'Text._text_rendered'
        db.delete_column('meetups_meetup_text', '_text_rendered')


    models = {
        'meetups.meetup': {
            'Meta': {'object_name': 'Meetup'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'meetups.text': {
            'Meta': {'ordering': "['ordering']", 'object_name': 'Text', 'db_table': "'meetups_meetup_text'"},
            '_text_rendered': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'text_set'", 'to': "orm['meetups.Meetup']"}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'text': ('markitup.fields.MarkupField', [], {'no_rendered_field': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['meetups']