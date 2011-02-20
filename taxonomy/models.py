from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.template.defaultfilters import slugify

###
### Managers
###
class TaxonomyManager(models.Manager):
    def get_for_object(self, obj):
        """
        Get all taxonomy type-term pairings for an instance of a content object.
        """
        ctype = ContentType.objects.get_for_model(obj)
        return self.filter(content_type__pk=ctype.pk,
                                 object_id=obj.pk)

    def get_dict_for_object(self, obj):
        """
        Get all taxonomy type-term pairs as a dict of strings
        """
        tax_list = self.get_for_object(obj)
        tax_dict = {}
        for taxon in tax_list:
            if taxon.term.taxonomy.type not in tax_dict:
                  tax_dict[taxon.term.taxonomy.type] = [taxon.term.term]
            else:
                  tax_dict[taxon.term.taxonomy.type].append(taxon.term.term)
        return tax_dict

    def get_objects_for_terms(self, terms, klass):
        """
        Get all objects of klass that have the specified terms attached
        """
        if type(terms) != list:
            terms = [terms]
        object_ctype = ContentType.objects.get_for_model(klass)
        object_ids = self.filter(term__in=terms, content_type=object_ctype).values_list(
                   'object_id', flat=True)
        return klass.objects.filter(id__in=object_ids)

    def get_for_object_and_taxonomy(self, obj, taxonomy):
        tdict = self.get_dict_for_object(obj)
        ret= tdict[taxonomy]
        return ret

###
### Models 
###

class Taxonomy(models.Model):
    """A facility for creating custom content classification types""" 
    type = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(blank=True)

    class Meta:
        verbose_name = "taxonomy"  
        verbose_name_plural = "taxonomies"

    def __unicode__(self): 
        return self.type

    def save(self, *args, **kwargs):
        if self.slug == "":
            self.slug = slugify(self.type)
        super(Taxonomy, self).save(*args, **kwargs)

class TaxonomyTerm(models.Model):
    """Terms are associated with a specific Taxonomy, and should be generically usable with any contenttype"""
    taxonomy = models.ForeignKey(Taxonomy, related_name='terms')
    term = models.CharField(max_length=50)
    slug = models.SlugField(blank=True)
    parent = models.ForeignKey('self', null=True,blank=True)

    class Meta:
        unique_together = ('taxonomy', 'term')
        ordering = ['taxonomy', 'term']

    def __unicode__(self):
        return self.term

    def save(self, *args, **kwargs):
        if self.slug == "":
            self.slug = slugify(self.type)
        super(TaxonomyTerm, self).save(*args, **kwargs)

class Taxon(models.Model):
    """Mappings between content and any taxonomy types/terms used to classify it"""
    term         = models.ForeignKey(TaxonomyTerm, db_index=True, related_name='taxa')
    content_type = models.ForeignKey(ContentType, verbose_name='content type', db_index=True)
    object_id    = models.PositiveIntegerField(db_index=True)    
    object       = generic.GenericForeignKey('content_type', 'object_id')

    objects = TaxonomyManager()

    class Meta:
        unique_together = ('term', 'content_type', 'object_id')
        verbose_name_plural = "Taxa"

    def __unicode__(self):
        return u'%s' % self.term


