# events/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('seminar/', views.seminar_view, name='seminar'),
    path('workshop/', views.workshop_view, name='workshop'),
    path('training/', views.training_view, name='training'),
    path('event/', views.event_view, name='event'),
    path('jobfair/', views.jobfair_view, name='job_fair'),
    path('webinar/', views.webinar_view, name='webinar'),
    path('podcast/', views.podcast_view, name='podcast'),
]
