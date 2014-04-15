# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'indexPage'
        db.delete_table(u'frontpage_indexpage')

        # Adding model 'FrontPage'
        db.create_table(u'frontpage_frontpage', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['frontpage.Page'], unique=True, primary_key=True)),
            ('frontPageCarousel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontpage.Carousel'], null=True, blank=True)),
        ))
        db.send_create_signal(u'frontpage', ['FrontPage'])


    def backwards(self, orm):
        # Adding model 'indexPage'
        db.create_table(u'frontpage_indexpage', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['frontpage.Page'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'frontpage', ['indexPage'])

        # Deleting model 'FrontPage'
        db.delete_table(u'frontpage_frontpage')


    models = {
        u'frontpage.background': {
            'Meta': {'object_name': 'Background'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'frontpage.carousel': {
            'Meta': {'object_name': 'Carousel'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['frontpage.Picture']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'template': ('django.db.models.fields.CharField', [], {'default': "'ROBOTCAROUSEL'", 'max_length': '200'})
        },
        u'frontpage.frontpage': {
            'Meta': {'ordering': "['-priority']", 'object_name': 'FrontPage', '_ormbases': [u'frontpage.Page']},
            'frontPageCarousel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontpage.Carousel']", 'null': 'True', 'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['frontpage.Page']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'frontpage.headerpicture': {
            'Meta': {'object_name': 'HeaderPicture'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'frontpage.page': {
            'Meta': {'ordering': "['-priority']", 'object_name': 'Page'},
            'carousel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontpage.Carousel']", 'null': 'True', 'blank': 'True'}),
            'html': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['frontpage.Picture']", 'null': 'True', 'blank': 'True'}),
            'name_on_navbar': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url_title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'frontpage.pagegroup': {
            'Meta': {'object_name': 'PageGroup'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pages': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['frontpage.Page']", 'null': 'True', 'blank': 'True'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'frontpage.picture': {
            'Meta': {'object_name': 'Picture'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'frontpage.robotpage': {
            'Meta': {'ordering': "['-priority']", 'object_name': 'RobotPage', '_ormbases': [u'frontpage.Page']},
            'carousel2': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontpage.Carousel']", 'null': 'True', 'blank': 'True'}),
            'challenge': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'challengeDescription': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'leagueType': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['frontpage.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'robotName': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['frontpage']