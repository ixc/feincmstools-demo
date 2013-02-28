# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MediaFileContent'
        db.create_table('meetups_meetup_mediafilecontent', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mediafile', self.gf('feincms.module.medialibrary.fields.MediaFileForeignKey')(related_name='+', to=orm['medialibrary.MediaFile'])),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='mediafilecontent_set', to=orm['meetups.Meetup'])),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ordering', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('type', self.gf('django.db.models.fields.CharField')(default='default', max_length=20)),
        ))
        db.send_create_signal('meetups', ['MediaFileContent'])

        # Adding model 'OEmbedContent'
        db.create_table('meetups_meetup_oembedcontent', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('oembed.fields.OEmbedField')(max_length=200)),
            ('width', self.gf('django.db.models.fields.PositiveIntegerField')(default=960, null=True, blank=True)),
            ('height', self.gf('django.db.models.fields.PositiveIntegerField')(default=540, null=True, blank=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='oembedcontent_set', to=orm['meetups.Meetup'])),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ordering', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('meetups', ['OEmbedContent'])

        # Adding model 'RawHTMLContent'
        db.create_table('meetups_meetup_rawhtmlcontent', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('html', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='rawhtmlcontent_set', to=orm['meetups.Meetup'])),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ordering', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('meetups', ['RawHTMLContent'])


    def backwards(self, orm):
        # Deleting model 'MediaFileContent'
        db.delete_table('meetups_meetup_mediafilecontent')

        # Deleting model 'OEmbedContent'
        db.delete_table('meetups_meetup_oembedcontent')

        # Deleting model 'RawHTMLContent'
        db.delete_table('meetups_meetup_rawhtmlcontent')


    models = {
        'medialibrary.category': {
            'Meta': {'ordering': "['parent__title', 'title']", 'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['medialibrary.Category']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '150'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'medialibrary.mediafile': {
            'Meta': {'ordering': "['-created']", 'object_name': 'MediaFile'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['medialibrary.Category']", 'null': 'True', 'blank': 'True'}),
            'copyright': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '255'}),
            'file_size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '12'})
        },
        'meetups.mediafilecontent': {
            'Meta': {'ordering': "['ordering']", 'object_name': 'MediaFileContent', 'db_table': "'meetups_meetup_mediafilecontent'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mediafile': ('feincms.module.medialibrary.fields.MediaFileForeignKey', [], {'related_name': "'+'", 'to': "orm['medialibrary.MediaFile']"}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'mediafilecontent_set'", 'to': "orm['meetups.Meetup']"}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'default'", 'max_length': '20'})
        },
        'meetups.meetup': {
            'Meta': {'object_name': 'Meetup'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'meetups.oembedcontent': {
            'Meta': {'ordering': "['ordering']", 'object_name': 'OEmbedContent', 'db_table': "'meetups_meetup_oembedcontent'"},
            'height': ('django.db.models.fields.PositiveIntegerField', [], {'default': '540', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'oembedcontent_set'", 'to': "orm['meetups.Meetup']"}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('oembed.fields.OEmbedField', [], {'max_length': '200'}),
            'width': ('django.db.models.fields.PositiveIntegerField', [], {'default': '960', 'null': 'True', 'blank': 'True'})
        },
        'meetups.rawhtmlcontent': {
            'Meta': {'ordering': "['ordering']", 'object_name': 'RawHTMLContent', 'db_table': "'meetups_meetup_rawhtmlcontent'"},
            'html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rawhtmlcontent_set'", 'to': "orm['meetups.Meetup']"}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255'})
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