from django import forms
from .models import Team, Membership

class TeamCreationForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ('name', 'description', 'parent_id')
    def clean(self):
        name = self.cleaned_data.get('name')
        parent_id = self.cleaned_data.get('parent_id')
        if parent_id is not None:
            if Team.objects.filter(id=parent_id).count() == 0:
                raise forms.ValidationError('Parent team does not exist')

class MembershipCreationForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = ('team_id', 'user_id', 'alumni', 'role_id')
    def clean(self):
        team_id = self.cleaned_data.get('team_id')
        user_id = self.cleaned_data.get('user_id')
        if Membership.objects.filter(team_id=team_id, user_id=user_id).count() > 0:
            raise forms.ValidationError('User is already a member of this team')
        

        