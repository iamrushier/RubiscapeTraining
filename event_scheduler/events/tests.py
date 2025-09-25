from django.test import TestCase
from django.contrib.auth.models import User
from .models import Event
from .forms import EventForm
from django.urls import reverse
import datetime

class EventModelTest(TestCase):
    def setUp(self):
        self.user=User.objects.create_user(username="abc",password="abc")
    
    def test_event_str(self):
        event=Event.objects.create(
            user=self.user,
            name="test",
            date=datetime.date.today(),
            time=datetime.time(12,0),
            description="testing"
        )
        self.assertEqual(str(event), f"test on {event.date} at {event.time}")

class EventFormTest(TestCase):
    def setUp(self):
        self.user=User.objects.create_user(username="abc",password="abc")
    
    def test_conflict_validation(self):
        Event.objects.create(
            user=self.user,
            name="Meeting",
            date=datetime.date.today(),
            time=datetime.time(10, 0),
            description="Test"
        )
        form = EventForm(
            data={
                "name":"second",
                "date":datetime.date.today(),
                "time":"10:00",
                "description":"conflict",
            },
            user=self.user
        )
        self.assertFalse(form.is_valid())
        self.assertIn("Err: You already have and event at this date and time", str(form.errors))
        
              
class EventViewTests(TestCase):
    def setUp(self):
        self.user=User.objects.create_user(username="testuser",password="q12we34r")
        self.client.login(username="testuser",password="q12we34r")
        
        self.event = Event.objects.create(
            user=self.user,
            name="test event",
            date=datetime.date.today(),
            time=datetime.time(10,0),
            description="description"
        )
    
    # View events
    def test_my_events_view(self):
        url = reverse("my_events")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,"events/my_events.html")
        self.assertContains(response, "test event")
    
    # Create event
    def test_create_event_view_get(self):
        url = reverse("create_event")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "events/create_event.html")

    def test_create_event_view_post(self):
        url = reverse("create_event")
        data = {
            "name": "New Event",
            "date": datetime.date.today(),
            "time": "12:00",
            "description": "Created via test"
        }
        response = self.client.post(url, data)
        self.assertRedirects(response, reverse("my_events"))
        self.assertTrue(Event.objects.filter(name="New Event", user=self.user).exists())
                
    # Update event  
    def test_update_event_view_get(self):
        url = reverse("update_event", args=[self.event.id])
        
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "events/update_event.html")
        self.assertContains(response, self.event.name) 

    def test_update_event_view_post(self):
        url = reverse("update_event", args=[self.event.id])
        data = {
            "name": "Updated Event",
            "date": self.event.date,
            "time": self.event.time.strftime("%H:%M"),
            "description": "Updated description"
        }
        response = self.client.post(url, data)
        self.assertRedirects(response, reverse("my_events"))
        self.event.refresh_from_db()
        self.assertEqual(self.event.name, "Updated Event")
    
    #Delete event
    def test_delete_event_view_get(self):
        url = reverse("delete_event", args=[self.event.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "events/delete_event.html")
        self.assertContains(response, self.event.name)
        
    def test_delete_event_view_post(self):
        url = reverse("delete_event", args=[self.event.id])
        response = self.client.post(url)
        self.assertRedirects(response, reverse("my_events"))
        self.assertFalse(Event.objects.filter(id=self.event.id).exists())