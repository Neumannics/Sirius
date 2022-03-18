from django.db import models

from team.models import Team

# Create your models here.
class Session(models.Model):
    CATEGORY_CHOICES = (
        ('N', 'Notice'),
        ('E', 'Event'),
        ('C', 'Class'),
    )
    DAYS_OF_WEEK = (
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
        (6, 'Sunday'),
    )
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES, default='N')
    start = models.DateTimeField()
    end = models.DateTimeField()
    day = models.CharField(max_length=1, choices=DAYS_OF_WEEK)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
