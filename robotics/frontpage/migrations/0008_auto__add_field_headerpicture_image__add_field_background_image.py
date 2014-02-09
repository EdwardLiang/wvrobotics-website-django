# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'HeaderPicture.image'
        db.add_column(u'frontpage_headerpicture', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(default=datetime.datetime(2014, 2, 9, 0, 0), max_length=100),
                      keep_default=False)

        # Removing M2M table for field images on 'HeaderPicture'
        db.delete_table('frontpage_headerpicture_images')

        # Adding field 'Background.image'
        db.add_column(u'frontpage_background', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(default=datetime.datetime(2014, 2, 9, 0, 0), max_length=100),
                      keep_default=False)

        # Removing M2M table for field image on 'Background'
        db.delete_table('frontpage_background_image')


    def backwards(self, orm):
        # Deleting field 'HeaderPicture.image'
        db.delete_column(u'frontpage_headerpicture', 'image')

        # Adding M2M table for field images on 'HeaderPicture'
        db.create_table(u'frontpage_headerpicture_images', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('headerpicture', models.ForeignKey(orm[u'frontpage.headerpicture'], null=False)),
            ('picture', models.ForeignKey(orm[u'frontpage.picture'], null=False))
        ))
        db.create_unique(u'frontpage_headerpicture_images', ['headerpicture_id', 'picture_id'])

        # Deleting field 'Background.image'
        db.delete_column(u'frontpage_background', 'image')

        # Adding M2M table for field image on 'Background'
        db.create_table(u'frontpage_background_image', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('background', models.ForeignKey(orm[u'frontpage.background'], null=False)),
            ('picture', models.ForeignKey(orm[u'frontpage.picture'], null=False))
        ))
        db.create_unique(u'frontpage_background_image', ['background_id', 'picture_id'])


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
        u'frontpage.headerpicture': {
            'Meta': {'object_name': 'HeaderPicture'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
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