# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'TaxonomyTerm.question'
        db.add_column(u'taxonomy_taxonomyterm', 'question',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=500, blank=True),
                      keep_default=False)

        # Adding field 'TaxonomyTerm.help_text'
        db.add_column(u'taxonomy_taxonomyterm', 'help_text',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=500, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'TaxonomyTerm.question'
        db.delete_column(u'taxonomy_taxonomyterm', 'question')

        # Deleting field 'TaxonomyTerm.help_text'
        db.delete_column(u'taxonomy_taxonomyterm', 'help_text')


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'taxonomy.taxonomy': {
            'Meta': {'object_name': 'Taxonomy'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'taxonomy.taxonomymap': {
            'Meta': {'unique_together': "(('term', 'content_type', 'object_id'),)", 'object_name': 'TaxonomyMap'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_index': 'True'}),
            'term': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'taxa'", 'to': u"orm['taxonomy.TaxonomyTerm']"})
        },
        u'taxonomy.taxonomyterm': {
            'Meta': {'ordering': "['taxonomy', 'term']", 'unique_together': "(('taxonomy', 'term', 'parent'),)", 'object_name': 'TaxonomyTerm'},
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'to': u"orm['taxonomy.TaxonomyTerm']", 'null': 'True', 'blank': 'True'}),
            'promoted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'blank': 'True'}),
            'taxonomy': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'taxonomyterm_terms'", 'to': u"orm['taxonomy.Taxonomy']"}),
            'term': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'weight': ('django.db.models.fields.PositiveIntegerField', [], {'default': '999'})
        }
    }

    complete_apps = ['taxonomy']