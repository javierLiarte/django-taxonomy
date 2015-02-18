# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Taxonomy'
        db.create_table(u'taxonomy_taxonomy', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, blank=True)),
        ))
        db.send_create_signal(u'taxonomy', ['Taxonomy'])

        # Adding model 'TaxonomyTerm'
        db.create_table(u'taxonomy_taxonomyterm', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('taxonomy', self.gf('django.db.models.fields.related.ForeignKey')(related_name='taxonomyterm_terms', to=orm['taxonomy.Taxonomy'])),
            ('term', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(to=orm['taxonomy.TaxonomyTerm'], null=True, blank=True)),
            ('promoted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('weight', self.gf('django.db.models.fields.PositiveIntegerField')(default=999)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, blank=True)),
            (u'lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal(u'taxonomy', ['TaxonomyTerm'])

        # Adding unique constraint on 'TaxonomyTerm', fields ['taxonomy', 'term', 'parent']
        db.create_unique(u'taxonomy_taxonomyterm', ['taxonomy_id', 'term', 'parent_id'])

        # Adding model 'TaxonomyMap'
        db.create_table(u'taxonomy_taxonomymap', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('term', self.gf('django.db.models.fields.related.ForeignKey')(related_name='taxa', to=orm['taxonomy.TaxonomyTerm'])),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.CharField')(max_length=128, db_index=True)),
        ))
        db.send_create_signal(u'taxonomy', ['TaxonomyMap'])

        # Adding unique constraint on 'TaxonomyMap', fields ['term', 'content_type', 'object_id']
        db.create_unique(u'taxonomy_taxonomymap', ['term_id', 'content_type_id', 'object_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'TaxonomyMap', fields ['term', 'content_type', 'object_id']
        db.delete_unique(u'taxonomy_taxonomymap', ['term_id', 'content_type_id', 'object_id'])

        # Removing unique constraint on 'TaxonomyTerm', fields ['taxonomy', 'term', 'parent']
        db.delete_unique(u'taxonomy_taxonomyterm', ['taxonomy_id', 'term', 'parent_id'])

        # Deleting model 'Taxonomy'
        db.delete_table(u'taxonomy_taxonomy')

        # Deleting model 'TaxonomyTerm'
        db.delete_table(u'taxonomy_taxonomyterm')

        # Deleting model 'TaxonomyMap'
        db.delete_table(u'taxonomy_taxonomymap')


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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'to': u"orm['taxonomy.TaxonomyTerm']", 'null': 'True', 'blank': 'True'}),
            'promoted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'blank': 'True'}),
            'taxonomy': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'taxonomyterm_terms'", 'to': u"orm['taxonomy.Taxonomy']"}),
            'term': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'weight': ('django.db.models.fields.PositiveIntegerField', [], {'default': '999'})
        }
    }

    complete_apps = ['taxonomy']