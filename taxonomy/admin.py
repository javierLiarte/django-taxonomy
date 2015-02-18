from django.contrib import admin
from django.contrib.contenttypes import generic
from taxonomy.models import Taxonomy, TaxonomyTerm, TaxonomyMap
from mptt.admin import MPTTModelAdmin

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

#class TaxonomyTermAdmin(admin.ModelAdmin):
#    list_display = ('term', 'taxonomy', 'parent')
#    list_filter = ['taxonomy']
#    search_fields = ('term',)
#    fieldsets = (
#        (None, {
#            'fields': ('taxonomy', 'term', 'parent',),
#        }),
#        ('Advanced', {
#            'fields': ('slug',),
#            'classes': ('collapse',),
#        }),
#    )
class TaxonomyTermAdmin(MPTTModelAdmin):
   list_display = ('term','type')
   list_filter = ('type',)

class TaxonomyMapAdmin(MPTTModelAdmin):
   pass


admin.site.register(Taxonomy, TaxonomyAdmin)
admin.site.register(TaxonomyTerm, TaxonomyTermAdmin)
admin.site.register(TaxonomyMap, TaxonomyMapAdmin)
