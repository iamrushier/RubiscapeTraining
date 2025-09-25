from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Event
from .forms import EventForm

@login_required
def my_events(request):
    events = Event.objects.filter(user=request.user).order_by('date','time')
    return render(request, 'events/my_events.html', {'events':events})


@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event= form.save(commit=False)
            event.user=request.user
            event.save()
            return redirect('my_events')
    else:
        form = EventForm()
    return render(request, 'events/create_event.html', {'form':form})