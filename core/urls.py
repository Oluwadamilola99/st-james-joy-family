from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.Soon.as_view(), name='soon'),
]