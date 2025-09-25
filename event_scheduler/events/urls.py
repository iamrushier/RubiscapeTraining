from django.urls import path
from .views import my_events

urlpatterns = [
    path('',my_events,name='my_events')
]
