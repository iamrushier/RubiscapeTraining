from django.shortcuts import render, redirect, get_object_or_404
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
        form = EventForm(request.POST, user=request.user)
        if form.is_valid():
            event= form.save(commit=False)
            event.user=request.user
            event.save()
            return redirect('my_events')
    else:
        form = EventForm(user=request.user)
    return render(request, 'events/create_event.html', {'form':form})

@login_required
def update_event(request, event_id):
    event = get_object_or_404(Event, id=event_id, user=request.user)
    if request.method=='POST':
        form = EventForm(request.POST, instance=event, user=request.user)
        if form.is_valid():
            form.save()
            return redirect("my_events")
    else:
        form = EventForm(instance=event, user=request.user)
    return render(request, 'events/update_event.html', {'form':form})

@login_required
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id, user=request.user)
    if request.method=="POST":
        event.delete()
        return redirect("my_events")
    return render(request, "events/delete_event.html", {'event':event})