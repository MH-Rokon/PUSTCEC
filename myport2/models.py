from django.db import models
from myport.models import Profile

# Certifications Section
class Certification(models.Model):
    profile = models.ForeignKey(Profile, related_name='certifications', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)
    issuer = models.CharField(max_length=255, blank=True, null=True)
    issue_date = models.DateField(blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)
    certificate_url = models.URLField(blank=True, null=True)
    certificate_image = models.ImageField(upload_to='certificates/', blank=True, null=True)

    def __str__(self):
        return self.name

# Achievements Section
class Achievement(models.Model):
    profile = models.ForeignKey(Profile, related_name='achievements', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    date_awarded = models.DateField(blank=True, null=True)
    achievement_image = models.ImageField(upload_to='achievement/', blank=True, null=True)

    def __str__(self):
        return self.title

# Publications Section
class Publication(models.Model):
    profile = models.ForeignKey(Profile, related_name='publications', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True, null=True)
    publisher = models.CharField(max_length=255, blank=True, null=True)
    publication_date = models.DateField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

# Volunteer Experience Section
class VolunteerExperience(models.Model):
    profile = models.ForeignKey(Profile, related_name='volunteer_experiences', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True, null=True)
    organization = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} at {self.organization}"

# Award and Honor Section
class Award_and_Honor(models.Model):
    profile = models.ForeignKey(Profile, related_name='award_and_honor', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    date_awarded = models.DateField(blank=True, null=True)
    award_and_honor_image = models.ImageField(upload_to='award_and_honor/', blank=True, null=True)

    def __str__(self):
        return self.title
