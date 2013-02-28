# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Text'
        db.create_table('meetups_meetup_text', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='text_set', to=orm['meetups.Meetup'])),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ordering', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('meetups', ['Text'])


    def backwards(self, orm):
        # Deleting model 'Text'
        db.delete_table('meetups_meetup_text')


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
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'text_set'", 'to': "orm['meetups.Meetup']"}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['meetups']