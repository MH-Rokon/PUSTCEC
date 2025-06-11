from django.contrib import admin
from .models import Award_and_Honor, Certification, Achievement, Publication, VolunteerExperience

# Registering models without custom admin classes
admin.site.register(Certification)
admin.site.register(Achievement)
admin.site.register(Publication)
admin.site.register(VolunteerExperience)
admin.site.register(Award_and_Honor)
