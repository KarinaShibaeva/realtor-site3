from django.urls import path
from flats.views import flat_list_view

app_name = 'flats'

urlpatterns = [path("",flat_list_view, name="list"),
               ]

