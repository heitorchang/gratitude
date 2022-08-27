from datetime import datetime
from django import forms
from .models import EventType, Tag


class DateInput(forms.DateInput):
    input_type = 'date'


class EventForm(forms.Form):
    event_day = forms.DateField(widget=DateInput, initial=datetime.now().strftime('%Y-%m-%d'))
    event_type = forms.ModelChoiceField(queryset=EventType.objects.all())
    event_description = forms.CharField(label="Description")
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False, widget=forms.SelectMultiple(attrs={'size': 8}))
    new_tags_comma_separated = forms.CharField(required=False)
    stars = range(1, 6)
    star_rating = forms.ChoiceField(choices=list(zip(stars, ('\u2b50' * i for i in stars))))
