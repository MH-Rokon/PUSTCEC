from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile, Experience, Education, Skill, Project, Research
#  Certification, Achievement, Publication, VolunteerExperience

# Profile Section
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'headline', 'location', 'summary', 'profile_picture', 
            'github', 'linkedin', 'career_objective', 'languages_spoken', 'interests'
        ]
from django import forms
from .models import FeaturedItem

class FeaturedItemForm(forms.ModelForm):
    class Meta:
        model = FeaturedItem
        fields = ['title', 'description', 'link', 'media_file', 'item_type']

# Experience Section
class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['title', 'company', 'description', 'start_date', 'end_date']

# Education Section
class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['institution', 'degree', 'graduation_year']

# Skills Section
class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'institution']

# Projects Section
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'project_url', 'start_date', 'end_date']

# Research Section
class ResearchForm(forms.ModelForm):
    class Meta:
        model = Research
        fields = ['title', 'description', 'project_url']

# # Certifications Section
# class CertificationForm(forms.ModelForm):
#     class Meta:
#         model = Certification
#         fields = ['name', 'issuer', 'issue_date', 'expiration_date', 'certificate_url', 'certificate_image']

# # Achievements/Awards Section
# class AchievementForm(forms.ModelForm):
#     class Meta:
#         model = Achievement
#         fields = ['title', 'description', 'date_awarded']

# # Publications Section
# class PublicationForm(forms.ModelForm):
#     class Meta:
#         model = Publication
#         fields = ['title', 'publisher', 'publication_date', 'link']

# # Volunteer Experience Section
# class VolunteerExperienceForm(forms.ModelForm):
#     class Meta:
#         model = VolunteerExperience
#         fields = ['title', 'organization', 'start_date', 'end_date', 'description']

# Authentication Forms
class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
