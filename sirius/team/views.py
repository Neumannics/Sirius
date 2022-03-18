from django.shortcuts import render, redirect
from .forms import TeamCreationForm

def create_team(request):
    if request.method == 'POST':
        form = TeamCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        return render(request, 'create_team.html')
