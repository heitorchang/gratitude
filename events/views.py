from datetime import datetime, timedelta

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import Event, EventType, Tag
from .forms import EventForm


def index(request, days_back=7):
    return render(request, "events/index.html", {
        "events": Event.objects.filter(event_day__gt=datetime.now() - timedelta(days=days_back)),
    })


def tag(request, tag_name):
    return render(request, "events/index.html", {
        "events": Event.objects.filter(event_day__gt=datetime.now() - timedelta(days=30),
                                       tags__tag_text=tag_name),
    })


def month(request, year, month):
    return render(request, "events/index.html", {
        "events": Event.objects.filter(event_day__year=year, event_day__month=month)
    })


def search_words(request, days, words):
    return render(request, "events/index.html", {
        "events": Event.objects.filter(event_day__gt=datetime.now() - timedelta(days=days),
                                       event_description__icontains=words)
    })


def tag_days(request, days, tag_name):
    return render(request, "events/index.html", {
        "events": Event.objects.filter(event_day__gt=datetime.now() - timedelta(days=days),
                                       tags__tag_text=tag_name),
    })


def stars_between(request, days, lower_bound, upper_bound):
    return render(request, "events/index.html", {
        "events": Event.objects.filter(event_day__gt=datetime.now() - timedelta(days=days),
                                       star_rating__gte=lower_bound,
                                       star_rating__lte=upper_bound)
    })


def add(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event_day = form.cleaned_data['event_day']
            event_type = form.cleaned_data['event_type']
            event_description = form.cleaned_data['event_description']
            tags = form.cleaned_data['tags']
            new_tags_comma_separated = form.cleaned_data['new_tags_comma_separated']
            star_rating = form.cleaned_data['star_rating']

            new_event_tags = []

            # add existing tags
            for tag in tags:
                if tag:
                    new_event_tags.append(Tag.objects.get(tag_text=tag))

            for new_tag_name in new_tags_comma_separated.split(','):
                if new_tag_name:
                    tag_object, created = Tag.objects.get_or_create(tag_text=new_tag_name.strip())
                    new_event_tags.append(tag_object)

            new_event = Event.objects.create(
                event_day=event_day,
                event_type=EventType.objects.get(event_type_text=event_type),
                event_description=event_description,
                star_rating=int(star_rating),
            )
            new_event.tags.set(new_event_tags)
            new_event.save()

            return HttpResponseRedirect(reverse('events:index'))
    else:
        form = EventForm()

    return render(request, "events/add_form.html", {'form': form})


def month_form(request):
    return render(request, "events/month_form.html")


def search_form(request):
    return render(request, "events/search_form.html")
