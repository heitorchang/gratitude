import datetime
from django.db import models

# Create your models here.


class EventType(models.Model):
    event_type_text = models.CharField(max_length=80)

    def __str__(self):
        return self.event_type_text


class Tag(models.Model):
    tag_text = models.CharField(max_length=80)

    class Meta:
        ordering = ['tag_text']

    def __str__(self):
        return self.tag_text


class Event(models.Model):
    event_day = models.DateField(default=datetime.date.today)
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE)
    event_description = models.CharField(max_length=200)
    tags = models.ManyToManyField(Tag, blank=True)
    star_rating = models.IntegerField(default=1)

    class Meta:
        ordering = ['-event_day', '-id']

    def __str__(self):
        star = "\u2b50"
        return f"{self.event_day.strftime('%b. %d')} {self.star_rating * star} {self.event_type} {self.event_description}"
