from django import forms
from .models import Session


class SessionCreationFrom(forms.Modelfrom):
    class Meta:
        model = Session
        fields = ('type', 'title', 'description', 'team_id')
    def clean(self):
        type = self.cleaned_data.get('type')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        team_id = self.cleaned_data.get('team_id')
        if type is not None and title is not None and description is not None and team_id is not None:
            if Session.objects.filter(type=type, title=title, description=description, team_id=team_id).count() == 0:
                raise forms.ValidationError('Session already exists')
        else:
            raise forms.ValidationError('Session already exists')

