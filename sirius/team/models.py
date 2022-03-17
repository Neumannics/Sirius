from django.db import models
from django.contrib.auth import get_user_model
from authorization.models import Roles

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField()
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name

class Membership(models.Model):
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE)
    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    alumni = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='alumni')
    role_id = models.ForeignKey(Roles, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username