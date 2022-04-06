from django import forms
from .models import Role

class RoleCreationForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ('role_name', 'role_description', 'permissions')
    def clean(self):
        role_name = self.cleaned_data.get('role_name')
        role_description = self.cleaned_data.get('role_description')
        permissions = self.cleaned_data.get('permissions')

        if role_name is not None and team_id is not None and role_description is not None and permissions is not None:
            if Role.objects.filter(role_name=role_name, team_id=team_id).count() != 0:
                raise forms.ValidationError('Role already exists')
        else:
            raise forms.ValidationError('Some fields are missing')



