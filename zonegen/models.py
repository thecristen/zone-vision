"""Django Models"""
from __future__ import unicode_literals

# from django.db import models
from django.contrib.gis.db import models as gismodels

# Create your models here.
class Zone(gismodels.Model):
    """Represents a type of zoning along with geographic info"""
    zid = gismodels.AutoField(primary_key=True)
    code = gismodels.TextField(blank=True)
    name = gismodels.TextField(blank=True)
    keywords = gismodels.TextField(blank=True)
    description = gismodels.TextField(blank=True)
    geometry = gismodels.MultiPolygonField(null=True, blank=True)
    objects = gismodels.GeoManager()

    def __unicode__(self):
        # CB - Central Business
        return u"%s - %s" % (self.code, self.name)
