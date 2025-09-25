from django.urls import path
from .views import my_events,create_event

urlpatterns = [
    path('',my_events,name='my_events'),
    path('create/',create_event,name='create_event')
]
