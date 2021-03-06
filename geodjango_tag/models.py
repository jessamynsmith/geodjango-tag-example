from django.contrib.gis.db import models as gis_models
from django.contrib.gis.geos import GEOSGeometry
from django.db import models
from taggit.managers import TaggableManager


class TaggedLocation(models.Model):
    name = models.CharField(max_length=100)
    location = gis_models.PolygonField()
    tags = TaggableManager()

    def tags_text(self):
        tag_list = self.tags.all().values_list('name', flat=True)
        return ', '.join(tag_list)

    def get_location_geo_json(self):
        geometry = GEOSGeometry(self.location)
        return geometry.json

    def __str__(self):
        return '{}'.format(self.name)