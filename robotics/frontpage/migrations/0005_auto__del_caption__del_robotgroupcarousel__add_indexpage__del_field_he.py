# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Caption'
        db.delete_table(u'frontpage_caption')

        # Deleting model 'RobotGroupCarousel'
        db.delete_table(u'frontpage_robotgroupcarousel')

        # Adding model 'indexPage'
        db.create_table(u'frontpage_indexpage', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['frontpage.Page'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'frontpage', ['indexPage'])

        # Deleting field 'HeaderPicture.image'
        db.delete_column(u'frontpage_headerpicture', 'image')

        # Adding M2M table for field images on 'HeaderPicture'
        db.create_table(u'frontpage_headerpicture_images', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('headerpicture', models.ForeignKey(orm[u'frontpage.headerpicture'], null=False)),
            ('picture', models.ForeignKey(orm[u'frontpage.picture'], null=False))
        ))
        db.create_unique(u'frontpage_headerpicture_images', ['headerpicture_id', 'picture_id'])

        # Adding M2M table for field carousel on 'Page'
        db.create_table(u'frontpage_page_carousel', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('page', models.ForeignKey(orm[u'frontpage.page'], null=False)),
            ('carousel', models.ForeignKey(orm[u'frontpage.carousel'], null=False))
        ))
        db.create_unique(u'frontpage_page_carousel', ['page_id', 'carousel_id'])

        # Adding field 'Carousel.name'
        db.add_column(u'frontpage_carousel', 'name',
                      self.gf('django.db.models.fields.CharField')(default=datetime.datetime(2014, 2, 9, 0, 0), max_length=200),
                      keep_default=False)

        # Adding field 'Carousel.template'
        db.add_column(u'frontpage_carousel', 'template',
                      self.gf('django.db.models.fields.CharField')(default='ROBOTCAROUSEL', max_length=200),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'Caption'
        db.create_table(u'frontpage_caption', (
            ('text', self.gf('django.db.models.fields.CharField')(max_length=200)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'frontpage', ['Caption'])

        # Adding model 'RobotGroupCarousel'
        db.create_table(u'frontpage_robotgroupcarousel', (
            (u'carousel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['frontpage.Carousel'], unique=True, primary_key=True)),
            ('leagueType', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'frontpage', ['RobotGroupCarousel'])

        # Deleting model 'indexPage'
        db.delete_table(u'frontpage_indexpage')


        # User chose to not deal with backwards NULL issues for 'HeaderPicture.image'
        raise RuntimeError("Cannot reverse this migration. 'HeaderPicture.image' and its values cannot be restored.")
        # Removing M2M table for field images on 'HeaderPicture'
        db.delete_table('frontpage_headerpicture_images')

        # Removing M2M table for field carousel on 'Page'
        db.delete_table('frontpage_page_carousel')

        # Deleting field 'Carousel.name'
        db.delete_column(u'frontpage_carousel', 'name')

        # Deleting field 'Carousel.template'
        db.delete_column(u'frontpage_carousel', 'template')


    models = {
        u'frontpage.carousel': {
            'Meta': {'object_name': 'Carousel'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['frontpage.Picture']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'template': ('django.db.models.fields.CharField', [], {'default': "'ROBOTCAROUSEL'", 'max_length': '200'})
        },
        u'frontpage.headerpicture': {
            'Meta': {'object_name': 'HeaderPicture'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['frontpage.Picture']", 'null': 'True', 'blank': 'True'})
        },
        u'frontpage.indexpage': {
            'Meta': {'object_name': 'indexPage', '_ormbases': [u'frontpage.Page']},
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['frontpage.Page']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'frontpage.page': {
            'Meta': {'object_name': 'Page'},
            'carousel': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['frontpage.Carousel']", 'null': 'True', 'blank': 'True'}),
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
        u'frontpage.robotpage': {
            'Meta': {'object_name': 'RobotPage', '_ormbases': [u'frontpage.Page']},
            'challenge': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'leagueType': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['frontpage.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'robotName': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['frontpage']