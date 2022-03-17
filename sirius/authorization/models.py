from django.db import models
from team.models import Team

# Create your models here.
class Roles(models.Model):
    role_name = models.CharField(max_length=100)
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE)
    role_description = models.CharField(max_length=100)

    def __str__(self):
        return self.role_name

class Permissions(models.Model):
    ACTION_CHOICES = (
        ('C', 'Create'),
        ('R', 'Read'),
        ('U', 'Update'),
        ('D', 'Delete'),
    )
    RELATION_CHOICES = (
        ('T', 'Team'),
        ('R', 'Role'),
        ('P', 'Permission'),
        ('S', 'Session'),
        ('M', 'Membership'),
    )
    role_id = models.ForeignKey(Roles, on_delete=models.CASCADE)
    permission_name = models.CharField(max_length=1, choices= ACTION_CHOICES)
    relation_name = models.CharField(max_length=1, choices= RELATION_CHOICES)

    def __str__(self):
        return self.permission_name
