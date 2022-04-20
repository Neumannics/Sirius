from django.db import models

from team.models import Team
from django.contrib.auth import get_user_model

# Create your models here.
class Session(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE)
    description = models.TextField()
    def __str__(self):
        return self.title

class Class(Session):
    DAYS_OF_WEEK = (
        ('0', 'Monday'),
        ('1', 'Tuesday'),
        ('2', 'Wednesday'),
        ('3', 'Thursday'),
        ('4', 'Friday'),
        ('5', 'Saturday'),
        ('6', 'Sunday'),
    )
    start_time = models.TimeField()
    end_time = models.TimeField()
    day = models.CharField(max_length=1, choices=DAYS_OF_WEEK)
    def __str__(self):
        return self.title

class Notice(Session):
    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Event(Session):
    start = models.DateTimeField()
    end = models.DateTimeField()
    def __str__(self):
        return self.title
