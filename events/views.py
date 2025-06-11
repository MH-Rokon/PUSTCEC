from datetime import date
from django.shortcuts import render
from .models import Seminar, Workshop, Training, Event, Podcast, Webinar, JobFair

# Helper function to categorize events
def categorize_events(model):
    today = date.today()
    
    # If the model has an event relationship, filter by related Event's date
    if hasattr(model, 'event'):
        events = model.objects.all()
        categorized_events = {
            'upcoming': events.filter(event__date__gte=today).order_by('event__date'),
            'previous': events.filter(event__date__lt=today).order_by('-event__date'),
        }
    else:
        # Fallback if no event relationship exists
        events = model.objects.all()
        categorized_events = {
            'upcoming': events.filter(date__gte=today).order_by('date'),
            'previous': events.filter(date__lt=today).order_by('-date'),
        }
    
    return categorized_events

# Views
def seminar_view(request):
    categorized_events = categorize_events(Seminar)
    return render(request, 'seminar.html', {'events': categorized_events})

def workshop_view(request):
    categorized_events = categorize_events(Workshop)
    return render(request, 'workshop.html', {'events': categorized_events})

def training_view(request):
    categorized_events = categorize_events(Training)
    return render(request, 'training.html', {'events': categorized_events})

def event_view(request):
    categorized_events = categorize_events(Event)  
    return render(request, 'event.html', {'events': categorized_events})

def podcast_view(request):
    categorized_events = categorize_events(Podcast)
    return render(request, 'podcast.html', {'events': categorized_events})

def webinar_view(request):
    categorized_events = categorize_events(Webinar)
    return render(request, 'webinar.html', {'events': categorized_events})

def jobfair_view(request):
    categorized_events = categorize_events(JobFair)
    return render(request, 'jobfair.html', {'events': categorized_events})
