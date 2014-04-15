# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'CarouselPicture'
        db.delete_table(u'frontpage_carouselpicture')

        # Adding model 'RobotGroupCarousel'
        db.create_table(u'frontpage_robotgroupcarousel', (
            (u'carousel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['frontpage.Carousel'], unique=True, primary_key=True)),
            ('leagueType', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'frontpage', ['RobotGroupCarousel'])

        # Adding model 'RobotPage'
        db.create_table(u'frontpage_robotpage', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['frontpage.Page'], unique=True, primary_key=True)),
            ('robotName', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('challenge', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('leagueType', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'frontpage', ['RobotPage'])

        # Adding model 'Carousel'
        db.create_table(u'frontpage_carousel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'frontpage', ['Carousel'])

        # Adding M2M table for field images on 'Carousel'
        db.create_table(u'frontpage_carousel_images', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('carousel', models.ForeignKey(orm[u'frontpage.carousel'], null=False)),
            ('picture', models.ForeignKey(orm[u'frontpage.picture'], null=False))
        ))
        db.create_unique(u'frontpage_carousel_images', ['carousel_id', 'picture_id'])

        # Adding field 'Page.text'
        db.add_column(u'frontpage_page', 'text',
                      self.gf('django.db.models.fields.CharField')(max_length=2000, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'CarouselPicture'
        db.create_table(u'frontpage_carouselpicture', (
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'frontpage', ['CarouselPicture'])

        # Deleting model 'RobotGroupCarousel'
        db.delete_table(u'frontpage_robotgroupcarousel')

        # Deleting model 'RobotPage'
        db.delete_table(u'frontpage_robotpage')

        # Deleting model 'Carousel'
        db.delete_table(u'frontpage_carousel')

        # Removing M2M table for field images on 'Carousel'
        db.delete_table('frontpage_carousel_images')

        # Deleting field 'Page.text'
        db.delete_column(u'frontpage_page', 'text')


    models = {
        u'frontpage.caption': {
            'Meta': {'object_name': 'Caption'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'frontpage.carousel': {
            'Meta': {'object_name': 'Carousel'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['frontpage.Picture']", 'null': 'True', 'blank': 'True'})
        },
        u'frontpage.headerpicture': {
            'Meta': {'object_name': 'HeaderPicture'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'frontpage.page': {
            'Meta': {'object_name': 'Page'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['frontpage.Picture']", 'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'frontpage.pagegroup': {
            'Meta': {'object_name': 'PageGroup'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pages': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['frontpage.Page']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'frontpage.picture': {
            'Meta': {'object_name': 'Picture'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'frontpage.robotgroupcarousel': {
            'Meta': {'object_name': 'RobotGroupCarousel', '_ormbases': [u'frontpage.Carousel']},
            u'carousel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['frontpage.Carousel']", 'unique': 'True', 'primary_key': 'True'}),
            'leagueType': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'frontpage.robotpage': {
            'Meta': {'object_name': 'RobotPage', '_ormbases': [u'frontpage.Page']},
            'challenge': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'leagueType': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['frontpage.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'robotName': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['frontpage']