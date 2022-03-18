from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import AccountAuthenticationForm, AccountSignupForm
from django.contrib.auth import get_user_model
from team.models import Team
from authorization.models import Membership
from django.contrib.auth.decorators import login_required


def sign_up(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = AccountSignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = AccountSignupForm()
        return render(request, 'signup.html', {'form': form})


def sign_in(request):
    user = request.user
    if user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                return redirect('/')
    else:
        form = AccountAuthenticationForm()
    return render(request, 'signin.html', { 'form': form })

def sign_out(request):
    logout(request)
    return redirect('landing_path')

@login_required(login_url='user:sign_in')
def dashboard(request, pk):
    user = get_user_model().objects.get(pk=pk).values('email', 'first_name', 'last_name')
    teams = Membership.objects.filter(user_id=pk).values('created_at', 'alumni', 'team_id__pk', 'team_id__name', 'role_id__pk', 'role_id__name')
    return render(request, 'dashboard.html', {'user': user, 'teams': teams})
            