from django.db import models
from datetime import datetime
from django.template.defaultfilters import truncatechars

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=1000)
    def __str__(self) -> str:
        return self.name
class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)
    def __str__(self) -> str:
        return self.user +" -- "+ self.value + " - " + self.room
    
    @property
    def short_value(self):
        return truncatechars(self.value, 75)
    
    def get_date(self):
        time = datetime.now()
        if self.date.day == time.day:
            return str(time.hour - self.date.hour) + " hours ago"
        else:
            if self.date.month == time.month:
                return str(time.day - self.date.day) + " days ago"
            else:
                if self.date.year == time.year:
                    return str(time.month - self.date.month) + " months ago"
        return self.date