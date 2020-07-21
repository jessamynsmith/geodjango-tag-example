from django.contrib.gis.db import models as gis_models
from django.db import models
from taggit.managers import TaggableManager


class TaggedLocation(models.Model):
    name = models.CharField(max_length=100)
    location = gis_models.PolygonField()
    tags = TaggableManager()
