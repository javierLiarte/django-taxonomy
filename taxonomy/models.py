from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey
from django.core.exceptions import ValidationError

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


###
### Models 
###

class Taxonomy(models.Model):
   """A facility for creating custom content classification types""" 
   type = models.CharField(max_length=50, unique=True)

   class Meta:
      verbose_name = "taxonomy"  
      verbose_name_plural = "taxonomies"

   def __unicode__(self): 
      return self.type

class TaxonomyTerm(MPTTModel):
   """Terms are associated with a specific Taxonomy, and should be generically usable with any contenttype"""
   type = models.ForeignKey(Taxonomy)
   term = models.CharField(max_length=50)
   parent = TreeForeignKey('self', null=True,blank=True)

   class Meta:
      unique_together = ('type', 'term')

   def __unicode__(self):
      return self.term
   
   def clean(self):
      if self.parent:
         if self.parent.type != self.type:
            raise ValidationError("Both parent and this term must "
            "share the same taxonomy!\n"
            "Current: {}, {}".format(self.parent.type,self.type))

class TaxonomyMap(models.Model):
   """Mappings between content and any taxonomy types/terms used to classify it"""
   term        = models.ForeignKey(TaxonomyTerm, db_index=True)
   type        = models.ForeignKey(Taxonomy, db_index=True)
   content_type = models.ForeignKey(ContentType, verbose_name='content type', db_index=True)
   object_id      = models.PositiveIntegerField(db_index=True)   
   object         = generic.GenericForeignKey('content_type', 'object_id')

   objects = TaxonomyManager()

   class Meta:
      unique_together = ('term', 'type', 'content_type', 'object_id')

   def __unicode__(self):
      return u'%s [%s]' % (self.term, self.type)

   def clean(self):
      if self.term.type != self.type:
         raise ValidationError("Term must belong to the same taxonomy! Current: {},{}".format(self.type,self.term.type))
