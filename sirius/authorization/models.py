from django.db import models
from team.models import Team

class Role(models.Model):
    role_name = models.CharField(max_length=100)
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE)
    role_description = models.CharField(max_length=100)
    permissions = models.TextField(default="1,")

    def __str__(self):
        return self.role_name
        
class Permission(models.Model):
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
    action = models.CharField(max_length=1, choices= ACTION_CHOICES)
    relation = models.CharField(max_length=1, choices= RELATION_CHOICES)

    def __str__(self):
        return self.action + " " + self.relation
