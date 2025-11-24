from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USER_TYPE_CHOICES=(
        ('admin','Admin'),
        ('user','User'),
    )
    user_type=models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='user')

    def __str__(self):
        return self.username

class Event(models.Model):
    title= models.CharField(max_length=100)
    description= models.TextField()
    date= models.DateField()
    location= models.CharField(max_length=60)
    created_by= models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_events")
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering= ['-date']
    
class EventInterest(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name="event_interests")
    event= models.ForeignKey(Event, on_delete=models.CASCADE, related_name="event_interests")
    interested_at= models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together= ('user', 'event')
        ordering= ['-interested_at']
    
    def __str__(self):
        return f"{self.user.username} - {self.event.title}"
