from django import forms
from django.conf import settings
from django.contrib.gis.forms.widgets import OSMWidget

from geodjango_tag import models as geodjango_tag_models


class TaggedLocationForm(forms.ModelForm):

    class Meta:
        model = geodjango_tag_models.TaggedLocation
        fields = ['name', 'location', 'tags']

        widgets = {
            'location': OSMWidget
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['location'].widget.attrs['default_zoom'] = settings.DEFAULT_ZOOM
        self.fields['location'].widget.attrs['default_lon'] = settings.DEFAULT_LOCATION['longitude']
        self.fields['location'].widget.attrs['default_lat'] = settings.DEFAULT_LOCATION['latitude']
