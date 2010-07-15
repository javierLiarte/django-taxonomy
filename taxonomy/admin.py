from django import forms
from django.contrib import admin
from django.contrib.contenttypes import generic
from taxonomy.models import Taxonomy, TaxonomyTerm, Taxon
from django.core.exceptions import ValidationError

class TaxonInlineFormset(generic.BaseGenericInlineFormSet):
    def clean(self):
        ll = map(str, filter(bool, self.cleaned_data))
        # setlist and ll may be in different orders
        ll.sort()
        setlist = list(set(ll))
        setlist.sort()
        if ll != setlist:
            raise ValidationError("Taxa must be unique.")

class TaxonInline(generic.GenericStackedInline):
    model = Taxon
    fields = ['term',]



    formset = TaxonInlineFormset





class TaxonomyAdmin(admin.ModelAdmin):
   pass

class TaxonomyTermAdmin(admin.ModelAdmin):
   pass

class TaxonAdmin(admin.ModelAdmin):
   pass


admin.site.register(Taxonomy, TaxonomyAdmin)
admin.site.register(TaxonomyTerm, TaxonomyTermAdmin)
#admin.site.register(Taxon, TaxonAdmin)
