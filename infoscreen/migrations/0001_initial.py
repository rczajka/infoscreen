# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'InfoBox'
        db.create_table('infoscreen_infobox', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('body', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('seconds', self.gf('django.db.models.fields.IntegerField')(default=30)),
            ('stamp', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('infoscreen', ['InfoBox'])


    def backwards(self, orm):
        # Deleting model 'InfoBox'
        db.delete_table('infoscreen_infobox')


    models = {
        'infoscreen.infobox': {
            'Meta': {'object_name': 'InfoBox'},
            'body': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seconds': ('django.db.models.fields.IntegerField', [], {'default': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'stamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['infoscreen']