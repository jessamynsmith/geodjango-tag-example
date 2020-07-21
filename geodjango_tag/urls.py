from django.urls import path

from geodjango_tag import views


urlpatterns = [
    path('locations/', views.TaggedLocationListView.as_view(), name='tagged_location_list'),
    path('locations/create/', views.TaggedLocationCreateView.as_view(),
         name='tagged_location_create'),
]
