import re

from django.conf import settings
from django.core.serializers import serialize
from django.db import models
from django.views.generic import CreateView, DetailView, ListView
from django.urls import reverse_lazy
from jsonview.views import JsonView

from geodjango_tag import forms as geodjango_tag_forms
from geodjango_tag import models as geodjango_tag_models


class TaggedLocationListView(ListView):
    model = geodjango_tag_models.TaggedLocation

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('name')
        self.query = self.request.GET.get('query')
        if self.query:
            query_args = re.split(r'[,\s]+', self.query)
            tag_q = models.Q(tags__name__in=query_args)
            queryset = queryset.filter(tag_q)
            queryset = queryset.annotate(num_tags=models.Count(
                'tags', filter=tag_q))
            queryset = queryset.order_by('-num_tags')
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['query'] = self.query
        return context_data


class TaggedLocationDetailView(DetailView):
    model = geodjango_tag_models.TaggedLocation

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['zoom'] = settings.DEFAULT_ZOOM
        context_data['location'] = settings.DEFAULT_LOCATION
        return context_data


class TaggedLocationCreateView(CreateView):
    model = geodjango_tag_models.TaggedLocation
    form_class = geodjango_tag_forms.TaggedLocationForm
    success_url = reverse_lazy('tagged_location_list')


class TaggedLocationJsonView(JsonView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        objects = geodjango_tag_models.TaggedLocation.objects.filter(pk=self.kwargs['pk'])
        context['data'] = serialize('geojson', objects)
        return context
