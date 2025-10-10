
from django.shortcuts import render, redirect
from post.models import Event, Project, Thesis
from itertools import chain
import random


def home(request):
    if request.user.is_authenticated:
        events = Event.objects.all()
        projects = Project.objects.all()
        theses = Thesis.objects.all()

        for e in events:
            e.content_type = "Event"
            e.date_field = e.created_at
        for p in projects:
            p.content_type = "Project"
            p.date_field = p.created_at
        for t in theses:
            t.content_type = "Thesis"
            t.date_field = t.created_at

        feed_items = list(chain(events, projects, theses))

        # 🎲 Add slight random variation to sort key
        def sort_key(item):
            # Random factor between -300 and +300 seconds (±5 minutes)
            random_offset = random.uniform(-300, 300)
            # Apply offset to timestamp
            return item.date_field.timestamp() + random_offset

        # Sort by adjusted key descending (newer + randomness)
        feed_items.sort(key=sort_key, reverse=True)


        return render(request, "home.html",{'feed_items':feed_items})
    else:
        return redirect("user:login_user")