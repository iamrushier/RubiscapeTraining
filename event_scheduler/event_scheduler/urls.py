from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from events import views as event_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', event_views.register, name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='events/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='events/logout.html'), name='logout'),
    path('', include('events.urls')),
]
