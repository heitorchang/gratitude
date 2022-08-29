import datetime
from django import forms
from .models import EventType, Tag


class DateInput(forms.DateInput):
    input_type = 'date'


class EventForm(forms.Form):
    event_day = forms.DateField(widget=DateInput, initial=datetime.date.today)
    event_type = forms.ModelChoiceField(queryset=EventType.objects.all(), initial=0)
    event_description = forms.CharField(label="Description", widget=forms.Textarea(attrs={'rows': 2, 'cols': 45}))
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False, widget=forms.SelectMultiple(attrs={'size': 8}))
    new_tags_comma_separated = forms.CharField(required=False)
    stars = range(1, 6)
    star_rating = forms.ChoiceField(choices=list(zip(stars, ('\u2b50' * i for i in stars))))
