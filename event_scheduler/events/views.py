from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Event
from .forms import EventForm

@login_required
def my_events(request):
    events = Event.objects.filter(user=request.user).order_by('date','time')
    return render(request, 'events/my_events.html', {'events':events})
