from django.urls import path
from .views import my_events,create_event,update_event,delete_event

urlpatterns = [
    path('',my_events,name='my_events'),
    path('create/',create_event,name='create_event'),
    path('update/<int:event_id>/',update_event,name='update_event'),
    path('delete/<int:event_id>/',delete_event,name='delete_event'),
]
