from django.contrib import admin
from .models import Seminar, Workshop, Training, Event, Webinar,JobFair,Podcast

# Register each model separately
admin.site.register(Event)
admin.site.register(Seminar)
admin.site.register(Workshop)
admin.site.register(Training)
admin.site.register(Podcast)
admin.site.register(JobFair)
admin.site.register( Webinar)
