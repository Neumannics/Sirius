from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import AccountAuthenticationForm, AccountSignupForm
from django.contrib.auth import get_user_model


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

def dashboard(request, pk):
    user = get_user_model().objects.get(pk=pk)
    return render(request, 'dashboard.html', {'user': user})
            