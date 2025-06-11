from django.db import models

class Event(models.Model):
    # Basic event details
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    venue = models.CharField(max_length=255)
    image = models.ImageField(upload_to='uploads/events/', blank=True, null=True)
    
    # Common fields
    organizer = models.CharField(max_length=200, blank=True, null=True)  # Optional
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.title} - {self.date}"

class Seminar(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE, related_name='seminar')
    speaker = models.CharField(max_length=200)
    topic = models.CharField(max_length=255)

    def __str__(self):
        return f"Seminar: {self.event.title} - {self.speaker}"

class Workshop(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE, related_name='workshop')
    facilitator = models.CharField(max_length=200)
    duration = models.CharField(max_length=50)

    def __str__(self):
        return f"Workshop: {self.event.title} - {self.facilitator}"

class Training(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE, related_name='training')
    trainer = models.CharField(max_length=200)
    training_field = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return f"Training: {self.event.title} - {self.trainer}"
    
    
class Webinar(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE, related_name='webinar')
    trainer = models.CharField(max_length=200)
    training_field = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return f"Webinar: {self.event.title} - {self.trainer}"

class Podcast(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE, related_name='podcast')
    trainer = models.CharField(max_length=200)
    topic = models.CharField(max_length=255)
    duration = models.DurationField()

    def __str__(self):
        return f"Podcast: {self.event.title} - {self.trainer}"
    
class JobFair(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE, related_name='jobfair')
    coordinator = models.CharField(max_length=200)
    industry_focus = models.CharField(max_length=255)
    number_of_companies = models.PositiveIntegerField()

    def __str__(self):
        return f"Job Fair: {self.event.title} - {self.coordinator}"