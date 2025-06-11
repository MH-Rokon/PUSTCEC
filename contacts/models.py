from django.db import models

class Contact(models.Model):
    club_name = models.CharField(max_length=200)
    club_short_name = models.CharField(max_length=50)
    email = models.EmailField()
    location_image = models.ImageField(upload_to='contacts/media/uploads/', blank=True, null=True)
    phone = models.CharField(max_length=20)
    contact_time = models.CharField(max_length=100, blank=True, null=True) 

    def __str__(self):
        return f"{self.club_name} ({self.club_short_name})"
