# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RobotCarousel'
        db.create_table(u'frontpage_robotcarousel', (
            (u'carousel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['frontpage.Carousel'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'frontpage', ['RobotCarousel'])

        # Adding model 'RobotBottomCarousel'
        db.create_table(u'frontpage_robotbottomcarousel', (
            (u'carousel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['frontpage.Carousel'], unique=True, primary_key=True)),
            ('header_title', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'frontpage', ['RobotBottomCarousel'])

        # Adding M2M table for field robot_pages on 'RobotBottomCarousel'
        db.create_table(u'frontpage_robotbottomcarousel_robot_pages', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('robotbottomcarousel', models.ForeignKey(orm[u'frontpage.robotbottomcarousel'], null=False)),
            ('robotpage', models.ForeignKey(orm[u'frontpage.robotpage'], null=False))
        ))
        db.create_unique(u'frontpage_robotbottomcarousel_robot_pages', ['robotbottomcarousel_id', 'robotpage_id'])

        # Adding model 'FrontPageCarousel'
        db.create_table(u'frontpage_frontpagecarousel', (
            (u'carousel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['frontpage.Carousel'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'frontpage', ['FrontPageCarousel'])

        # Deleting field 'Page.carousel'
        db.delete_column(u'frontpage_page', 'carousel_id')

        # Deleting field 'RobotPage.robotName'
        db.delete_column(u'frontpage_robotpage', 'robotName')

        # Deleting field 'RobotPage.carousel2'
        db.delete_column(u'frontpage_robotpage', 'carousel2_id')

        # Adding field 'RobotPage.robot_carousel'
        db.add_column(u'frontpage_robotpage', 'robot_carousel',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontpage.RobotCarousel'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'RobotPage.robot_bottom_carousel'
        db.add_column(u'frontpage_robotpage', 'robot_bottom_carousel',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontpage.RobotBottomCarousel'], null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Carousel.template'
        db.delete_column(u'frontpage_carousel', 'template')


    def backwards(self, orm):
        # Deleting model 'RobotCarousel'
        db.delete_table(u'frontpage_robotcarousel')

        # Deleting model 'RobotBottomCarousel'
        db.delete_table(u'frontpage_robotbottomcarousel')

        # Removing M2M table for field robot_pages on 'RobotBottomCarousel'
        db.delete_table('frontpage_robotbottomcarousel_robot_pages')

        # Deleting model 'FrontPageCarousel'
        db.delete_table(u'frontpage_frontpagecarousel')

        # Adding field 'Page.carousel'
        db.add_column(u'frontpage_page', 'carousel',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontpage.Carousel'], null=True, blank=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'RobotPage.robotName'
        raise RuntimeError("Cannot reverse this migration. 'RobotPage.robotName' and its values cannot be restored.")
        # Adding field 'RobotPage.carousel2'
        db.add_column(u'frontpage_robotpage', 'carousel2',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontpage.Carousel'], null=True, blank=True),
                      keep_default=False)

        # Deleting field 'RobotPage.robot_carousel'
        db.delete_column(u'frontpage_robotpage', 'robot_carousel_id')

        # Deleting field 'RobotPage.robot_bottom_carousel'
        db.delete_column(u'frontpage_robotpage', 'robot_bottom_carousel_id')

        # Adding field 'Carousel.template'
        db.add_column(u'frontpage_carousel', 'template',
                      self.gf('django.db.models.fields.CharField')(default='ROBOTCAROUSEL', max_length=200),
                      keep_default=False)


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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'frontpage.frontpage': {
            'Meta': {'ordering': "['-priority']", 'object_name': 'FrontPage', '_ormbases': [u'frontpage.Page']},
            'frontPageCarousel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontpage.Carousel']", 'null': 'True', 'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['frontpage.Page']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'frontpage.frontpagecarousel': {
            'Meta': {'object_name': 'FrontPageCarousel', '_ormbases': [u'frontpage.Carousel']},
            u'carousel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['frontpage.Carousel']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'frontpage.headerpicture': {
            'Meta': {'object_name': 'HeaderPicture'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'frontpage.page': {
            'Meta': {'ordering': "['-priority']", 'object_name': 'Page'},
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
            'Meta': {'ordering': "['-priority']", 'object_name': 'PageGroup'},
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
        u'frontpage.robotbottomcarousel': {
            'Meta': {'object_name': 'RobotBottomCarousel', '_ormbases': [u'frontpage.Carousel']},
            u'carousel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['frontpage.Carousel']", 'unique': 'True', 'primary_key': 'True'}),
            'header_title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'robot_pages': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['frontpage.RobotPage']", 'null': 'True', 'blank': 'True'})
        },
        u'frontpage.robotcarousel': {
            'Meta': {'object_name': 'RobotCarousel', '_ormbases': [u'frontpage.Carousel']},
            u'carousel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['frontpage.Carousel']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'frontpage.robotpage': {
            'Meta': {'ordering': "['-priority']", 'object_name': 'RobotPage', '_ormbases': [u'frontpage.Page']},
            'challenge': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'challengeDescription': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'leagueType': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['frontpage.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'robot_bottom_carousel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontpage.RobotBottomCarousel']", 'null': 'True', 'blank': 'True'}),
            'robot_carousel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontpage.RobotCarousel']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['frontpage']