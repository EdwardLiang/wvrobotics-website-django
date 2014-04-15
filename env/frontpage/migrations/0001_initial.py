# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Picture'
        db.create_table(u'frontpage_picture', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'frontpage', ['Picture'])

        # Adding model 'CarouselPicture'
        db.create_table(u'frontpage_carouselpicture', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'frontpage', ['CarouselPicture'])

        # Adding model 'HeaderPicture'
        db.create_table(u'frontpage_headerpicture', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'frontpage', ['HeaderPicture'])

        # Adding model 'Caption'
        db.create_table(u'frontpage_caption', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'frontpage', ['Caption'])

        # Adding model 'Page'
        db.create_table(u'frontpage_page', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('images', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontpage.Picture'], null=True, blank=True)),
        ))
        db.send_create_signal(u'frontpage', ['Page'])

        # Adding model 'PageGroup'
        db.create_table(u'frontpage_pagegroup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('pages', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontpage.Page'], null=True, blank=True)),
        ))
        db.send_create_signal(u'frontpage', ['PageGroup'])


    def backwards(self, orm):
        # Deleting model 'Picture'
        db.delete_table(u'frontpage_picture')

        # Deleting model 'CarouselPicture'
        db.delete_table(u'frontpage_carouselpicture')

        # Deleting model 'HeaderPicture'
        db.delete_table(u'frontpage_headerpicture')

        # Deleting model 'Caption'
        db.delete_table(u'frontpage_caption')

        # Deleting model 'Page'
        db.delete_table(u'frontpage_page')

        # Deleting model 'PageGroup'
        db.delete_table(u'frontpage_pagegroup')


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