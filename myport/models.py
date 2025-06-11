from django.db import models
from django.contrib.auth.models import User

# Profile Section
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255, blank=True, null=True)  # Career headline (optional)
    location = models.CharField(max_length=255, blank=True, null=True)  # Location (optional)
    summary = models.TextField(blank=True, null=True)  # Professional summary (optional)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)  # Profile picture (optional)
    github = models.URLField(blank=True, null=True)  # GitHub URL (optional)
    linkedin = models.URLField(blank=True, null=True)  # LinkedIn URL (optional)
    career_objective = models.TextField(blank=True, null=True)  # Career objective or professional summary (optional)
    languages_spoken = models.CharField(max_length=255, blank=True, null=True)  # Languages spoken (optional)
    interests = models.TextField(blank=True, null=True)  # Interests or hobbies (optional)

    def __str__(self):
        return self.user.username
from django.db import models
from django.contrib.auth.models import User

class FeaturedItem(models.Model):
    FEATURED_TYPE_CHOICES = [
        ('Post', 'Post'),
        ('Article', 'Article'),
        ('Link', 'Link'),
        ('Media', 'Media'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(blank=True, null=True)
    media_file = models.FileField(upload_to='featured_media/', blank=True, null=True)
    item_type = models.CharField(max_length=50, choices=FEATURED_TYPE_CHOICES)
    profile = models.ForeignKey(Profile, related_name='featured_items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Experience Section
class Experience(models.Model):
    profile = models.ForeignKey(Profile, related_name='experiences', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True, null=True)  # Job title (optional)
    company = models.CharField(max_length=255, blank=True, null=True)  # Company name (optional)
    description = models.TextField(blank=True, null=True)  # Description of the role (optional)
    start_date = models.DateField(blank=True, null=True)  # Start date of the experience (optional)
    end_date = models.DateField(blank=True, null=True)  # End date of the experience (optional)

    def __str__(self):
        return f"{self.title} at {self.company}"

# Education Section
class Education(models.Model):
    profile = models.ForeignKey(Profile, related_name='education', on_delete=models.CASCADE)
    institution = models.CharField(max_length=255, blank=True, null=True)  # Name of the institution (optional)
    degree = models.CharField(max_length=255, blank=True, null=True)  # Degree awarded (optional)
    graduation_year = models.IntegerField(blank=True, null=True)  # Year of graduation (optional)

    def __str__(self):
        return f"{self.degree} from {self.institution}"

# Skills Section
class Skill(models.Model):
    profile = models.ForeignKey(Profile, related_name='skills', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)  # Skill name (optional)
    institution= models.CharField(max_length=255, blank=True, null=True) 

    def __str__(self):
        return self.name

# Projects Section
class Project(models.Model):
    profile = models.ForeignKey(Profile, related_name='projects', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True, null=True)  # Project title (optional)
    description = models.TextField(blank=True, null=True)  # Project description (optional)
    project_url = models.URLField(blank=True, null=True)  # Link to the project (optional)
    start_date = models.DateField(blank=True, null=True)  # Project start date (optional)
    end_date = models.DateField(blank=True, null=True)  # Project end date (optional)

    def __str__(self):
        return self.title

# Research Section
class Research(models.Model):
    profile = models.ForeignKey(Profile, related_name='researches', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True, null=True)  # Research title (optional)
    description = models.TextField(blank=True, null=True)  # Research description (optional)
    project_url = models.URLField(blank=True, null=True)  # Link to the project (optional)

    def __str__(self):
        return self.title
