from django import forms
from .models import Class, Notice, Event


class ClassCreationForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ('start_time', 'end_time', 'day', 'title')
    def clean(self):
        start_time = self.cleaned_data.get('start_time')
        end_time = self.cleaned_data.get('end_time')
        day = self.cleaned_data.get('day')
        title = self.cleaned_data.get('title')

        if start_time is not None and end_time is not None and day is not None and title is not None:
            if Class.objects.filter(start_time__gte=start_time, end_time__lte=end_time).count() != 0:
                raise forms.ValidationError('Some classes overlap')
        else:
            raise forms.ValidationError('Some fields are missing')



    


class CalendarCreationForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('start', 'end', 'title', 'description')
    def clean(self):
        start = self.cleaned_data.get('start')
        end = self.cleaned_data.get('end')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')

        if start is not None and end is not None and title is not None and description is not None:
            if Event.objects.filter(start=start, end=end, title=title, description=description).count() != 0:
                raise forms.ValidationError('Event already exists')
        else:
            raise forms.ValidationError('Some fields are missing')
        



class NoticeCreationForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ('title', 'description')
    def clean(self):
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')

        if title is not None and description is not None:
            if Notice.objects.filter(title=title, description=description).count() != 0:
                raise forms.ValidationError('Notice already exists')
        else:
            raise forms.ValidationError('Some fields are missing')



