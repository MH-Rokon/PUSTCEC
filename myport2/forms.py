from django import forms
from django.contrib.auth.models import User
from myport2.models import  Certification, Achievement, Publication, VolunteerExperience,Award_and_Honor
from myport.forms import ProfileForm



# Certifications Section
class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = ['name', 'issuer', 'issue_date', 'expiration_date', 'certificate_url', 'certificate_image']

# Achievements/Awards Section
class AchievementForm(forms.ModelForm):
    class Meta:
        model = Achievement
        fields = ['title', 'description', 'date_awarded','achievement_image']

# Achievements/Awards Section
class Award_and_HonorForm(forms.ModelForm):
    class Meta:
        model = Award_and_Honor
        fields = ['title', 'description', 'date_awarded','award_and_honor_image']

# Publications Section
class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['title', 'publisher', 'publication_date', 'link']

# Volunteer Experience Section
class VolunteerExperienceForm(forms.ModelForm):
    class Meta:
        model = VolunteerExperience
        fields = ['title', 'organization', 'start_date', 'end_date', 'description']

