from django.contrib import admin
from taxonomy.models import Taxonomy, TaxonomyTerm, TaxonomyMap
from mptt.admin import MPTTModelAdmin

class TaxonomyAdmin(admin.ModelAdmin):
   pass

class TaxonomyTermAdmin(MPTTModelAdmin):
   list_display = ('term','type')
   list_filter = ('type',)

class TaxonomyMapAdmin(MPTTModelAdmin):
   pass


admin.site.register(Taxonomy, TaxonomyAdmin)
admin.site.register(TaxonomyTerm, TaxonomyTermAdmin)
admin.site.register(TaxonomyMap, TaxonomyMapAdmin)
