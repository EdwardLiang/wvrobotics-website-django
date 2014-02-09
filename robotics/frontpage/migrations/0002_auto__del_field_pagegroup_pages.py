# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'PageGroup.pages'
        db.delete_column(u'frontpage_pagegroup', 'pages_id')

        # Adding M2M table for field mainPage on 'PageGroup'
        db.create_table(u'frontpage_pagegroup_mainPage', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pagegroup', models.ForeignKey(orm[u'frontpage.pagegroup'], null=False)),
            ('page', models.ForeignKey(orm[u'frontpage.page'], null=False))
        ))
        db.create_unique(u'frontpage_pagegroup_mainPage', ['pagegroup_id', 'page_id'])


    def backwards(self, orm):
        # Adding field 'PageGroup.pages'
        db.add_column(u'frontpage_pagegroup', 'pages',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontpage.Page'], null=True, blank=True),
                      keep_default=False)

        # Removing M2M table for field mainPage on 'PageGroup'
        db.delete_table('frontpage_pagegroup_mainPage')


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
            'mainPage': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['frontpage.Page']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'frontpage.picture': {
            'Meta': {'object_name': 'Picture'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['frontpage']