from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType

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

   def get_taxonomy_dict_for_object(self, obj):
       """
       Get all taxonomy type-term pairings, as a dictionary
       """
       taxonomy_list = self.get_for_object(obj)
       taxonomy_dict = {}
       for t_item in taxonomy_list:
            if t_item.taxonomy not in taxonomy_dict:
                taxonomy_dict[t_item.taxonomy] = [t_item]
            else:
                taxonomy_dict[t_item.taxonomy].append(t_item)



###
### Models 
###

class Taxonomy(models.Model):
   """A facility for creating custom content classification types""" 
   name = models.CharField(max_length=50, unique=True)

   class Meta:
      verbose_name = "taxonomy"  
      verbose_name_plural = "taxonomies"

   def __unicode__(self): 
      return self.name

class TaxonomyTerm(models.Model):
   """Terms are associated with a specific Taxonomy, and should be generically usable with any contenttype"""
   taxonomy = models.ForeignKey(Taxonomy)
   term = models.CharField(max_length=50)
   parent = models.ForeignKey('self', null=True,blank=True)

   class Meta:
      unique_together = ('taxonomy', 'term')

   def __unicode__(self):
      return u"%s [%s]" % (self.term, self.taxonomy)

class Taxon(models.Model):
   """Mappings between content and any taxonomy types/terms used to classify it"""
   term        = models.ForeignKey(TaxonomyTerm, db_index=True)
   content_type = models.ForeignKey(ContentType, verbose_name='content type', db_index=True)
   object_id      = models.PositiveIntegerField(db_index=True)   
   object         = generic.GenericForeignKey('content_type', 'object_id')

   objects = TaxonomyManager()


   class Meta:
      unique_together = ('term', 'content_type', 'object_id')
      verbose_name_plural = "Taxa"



   def __unicode__(self):
      return u'%s' % self.term


