from django.test import TestCase
from django.contrib.auth.models import User
from .models import Event
from .forms import EventForm
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