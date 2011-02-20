from django.contrib import admin
from django.contrib.contenttypes import generic
from django.core.exceptions import ValidationError
from taxonomy.models import Taxonomy, TaxonomyTerm, Taxon

class TaxonInline(generic.GenericStackedInline):
    model = Taxon
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

class TaxonomyTermAdmin(admin.ModelAdmin):
    list_display = ('term', 'taxonomy', 'parent')
    list_filter = ['taxonomy']
    fieldsets = (
        (None, {
            'fields': ('taxonomy', 'term', 'parent',),
        }),
        ('Advanced', {
            'fields': ('slug',),
            'classes': ('collapse',),
        }),
    )

class TaxonAdmin(admin.ModelAdmin):
   pass


admin.site.register(Taxonomy, TaxonomyAdmin)
admin.site.register(TaxonomyTerm, TaxonomyTermAdmin)
admin.site.register(Taxon, TaxonAdmin)
