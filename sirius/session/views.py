from django.shortcuts import render, redirect
from .forms import SessionCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='user:sign_in')
def create_session(request):
    if request.method == 'POST':
        form = SessionCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SessionCreationForm()
    return render(request, 'session/create.html', {'form': form})
