# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'HorizontalRule'
        db.create_table('magazine_article_horizontalrule', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='horizontalrule_set', to=orm['magazine.Article'])),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ordering', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('magazine', ['HorizontalRule'])


    def backwards(self, orm):
        # Deleting model 'HorizontalRule'
        db.delete_table('magazine_article_horizontalrule')


    models = {
        'magazine.article': {
            'Meta': {'ordering': "['tree_id', 'lft']", 'object_name': 'Article'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['magazine.Article']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'template_key': ('django.db.models.fields.CharField', [], {'default': "'base'", 'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'magazine.horizontalrule': {
            'Meta': {'ordering': "['ordering']", 'object_name': 'HorizontalRule', 'db_table': "'magazine_article_horizontalrule'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'horizontalrule_set'", 'to': "orm['magazine.Article']"}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'magazine.mediafilecontent': {
            'Meta': {'ordering': "['ordering']", 'object_name': 'MediaFileContent', 'db_table': "'magazine_article_mediafilecontent'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mediafile': ('feincms.module.medialibrary.fields.MediaFileForeignKey', [], {'related_name': "'+'", 'to': "orm['medialibrary.MediaFile']"}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'mediafilecontent_set'", 'to': "orm['magazine.Article']"}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'default'", 'max_length': '20'})
        },
        'magazine.oembedcontent': {
            'Meta': {'ordering': "['ordering']", 'object_name': 'OEmbedContent', 'db_table': "'magazine_article_oembedcontent'"},
            'height': ('django.db.models.fields.PositiveIntegerField', [], {'default': '540', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'oembedcontent_set'", 'to': "orm['magazine.Article']"}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('oembed.fields.OEmbedField', [], {'max_length': '200'}),
            'width': ('django.db.models.fields.PositiveIntegerField', [], {'default': '960', 'null': 'True', 'blank': 'True'})
        },
        'magazine.rawhtmlcontent': {
            'Meta': {'ordering': "['ordering']", 'object_name': 'RawHTMLContent', 'db_table': "'magazine_article_rawhtmlcontent'"},
            'html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rawhtmlcontent_set'", 'to': "orm['magazine.Article']"}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'magazine.relatedarticle': {
            'Meta': {'ordering': "['ordering']", 'object_name': 'RelatedArticle', 'db_table': "'magazine_article_relatedarticle'"},
            'article': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['magazine.Article']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'relatedarticle_set'", 'to': "orm['magazine.Article']"}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'magazine.text': {
            'Meta': {'ordering': "['ordering']", 'object_name': 'Text', 'db_table': "'magazine_article_text'"},
            '_text_rendered': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'text_set'", 'to': "orm['magazine.Article']"}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'text': ('markitup.fields.MarkupField', [], {'no_rendered_field': 'True', 'blank': 'True'})
        },
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
        }
    }

    complete_apps = ['magazine']