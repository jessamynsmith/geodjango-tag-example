from django.views.generic import CreateView, DetailView, ListView
from django.urls import reverse_lazy
from geodjango_tag import models as geodjango_tag_models


class TaggedLocationListView(ListView):
    model = geodjango_tag_models.TaggedLocation


class TaggedLocationDetailView(DetailView):
    model = geodjango_tag_models.TaggedLocation


class TaggedLocationCreateView(CreateView):
    model = geodjango_tag_models.TaggedLocation
    fields = ['name', 'location', 'tags']
    success_url = reverse_lazy('tagged_location_list')

