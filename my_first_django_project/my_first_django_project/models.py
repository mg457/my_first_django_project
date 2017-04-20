from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=400)

    @classmethod
    def create(cls, title, description):
        event = cls(title=title, description=description)
        # do something with the book
        return event

event = Event.create("Party", "party description")