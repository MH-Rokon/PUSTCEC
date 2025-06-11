from django.contrib import admin
from .models import Profile, Experience, Education, Skill, Project, Research,FeaturedItem

# Registering models without custom admin classes
admin.site.register(Profile)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Research)
admin.site.register(FeaturedItem)
# admin.site.register(Certification)
# admin.site.register(Achievement)
# admin.site.register(Publication)
# admin.site.register(VolunteerExperience)
