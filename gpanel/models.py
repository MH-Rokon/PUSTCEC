from django.db import models

class ClubMember(models.Model):
    # Common fields for all members
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)  # Personal description or biography
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    # Social Media Links
    facebook_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    pustcesf_link = models.URLField(blank=True, null=True)

    # Role types (Founding Member, Executive, Advisor, etc.)
    ROLE_CHOICES = [
    ('Founder', 'Founder'),
    ('Executive', 'Executive'),
    ('Pre-Executive', 'Pre-Executive'),
    ('External Advisor', 'External Advisor'),  # Added External Advisor role
    ('Internal Advisor', 'Internal Advisor'),  # Added Internal role
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)


    # Fields for Advisors
    advisor_designation = models.CharField(max_length=255, blank=True, null=True)
    advisor_department = models.CharField(max_length=255, blank=True, null=True)  # Department/Faculty

    # Additional fields for Founding Members and Executives
    founding_date = models.DateField(null=True, blank=True)  # For Founding Members
    executive_work = models.CharField(max_length=255, blank=True, null=True)  # For Executives (where they work)

    # Contact Information
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    # Membership status (Active/Inactive)
    is_active = models.BooleanField(default=True)

    # Date of joining
    date_joined = models.DateField(null=True, blank=True)

    # Member visibility on website (boolean)
    is_visible_on_website = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.role}'

    class Meta:
        verbose_name = 'Club Member'
        verbose_name_plural = 'Club Members'
