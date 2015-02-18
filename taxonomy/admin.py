# coding: utf-8

from django.contrib import admin
from django.contrib.contenttypes import generic
from taxonomy.models import Taxonomy, TaxonomyTerm, TaxonomyMap
from mptt.admin import MPTTModelAdmin


class TaxonomyMapInline(generic.GenericStackedInline):
        model = TaxonomyMap
        fields = ['term']


class TaxonomyAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('type',),
        }),
        ('Advanced', {
            'fields': ('slug',),
            'classes': ('collapse',),
        }),
    )


class TaxonomyTermAdmin(MPTTModelAdmin):
    list_display = ('term', 'taxonomy', 'parent', 'promoted', 'weight')
    list_filter = ('taxonomy', 'promoted', 'parent',)
    search_fields = ('term',)
    fieldsets = (
        (None, {
            'fields': ('taxonomy', 'term', 'parent', 'promoted',),
        }),
        ('Advanced', {
            'fields': ('slug', 'weight',),
            'classes': ('collapse',),
        }),
    )
    tree_auto_open = True

class TaxonomyMapAdmin(admin.ModelAdmin):
    list_display = ('object', 'term',)
    pass


admin.site.register(Taxonomy, TaxonomyAdmin)
admin.site.register(TaxonomyTerm, TaxonomyTermAdmin)
admin.site.register(TaxonomyMap, TaxonomyMapAdmin)
