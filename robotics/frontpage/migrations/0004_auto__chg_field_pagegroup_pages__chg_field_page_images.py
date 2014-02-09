# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'PageGroup.pages'
        db.alter_column(u'frontpage_pagegroup', 'pages_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontpage.Page'], null=True))

        # Changing field 'Page.images'
        db.alter_column(u'frontpage_page', 'images_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontpage.Picture'], null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'PageGroup.pages'
        raise RuntimeError("Cannot reverse this migration. 'PageGroup.pages' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'PageGroup.pages'
        db.alter_column(u'frontpage_pagegroup', 'pages_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontpage.Page']))

        # User chose to not deal with backwards NULL issues for 'Page.images'
        raise RuntimeError("Cannot reverse this migration. 'Page.images' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Page.images'
        db.alter_column(u'frontpage_page', 'images_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontpage.Picture']))

    models = {
        u'frontpage.caption': {
            'Meta': {'object_name': 'Caption'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'frontpage.carouselpicture': {
            'Meta': {'object_name': 'CarouselPicture'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'frontpage.headerpicture': {
            'Meta': {'object_name': 'HeaderPicture'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'frontpage.page': {
            'Meta': {'object_name': 'Page'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontpage.Picture']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'frontpage.pagegroup': {
            'Meta': {'object_name': 'PageGroup'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pages': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontpage.Page']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'frontpage.picture': {
            'Meta': {'object_name': 'Picture'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['frontpage']