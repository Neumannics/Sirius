from django.shortcuts import render,redirect
from .forms import RoleCreationForm, PermissionCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.



# Create your views here.
@login_required(login_url='user:sign_in')
def create_role(request):
    if request.method == 'POST':
        form = RoleCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = RoleCreationForm()
    return render(request, 'create_role.html', {'form': form})

@login_required(login_url='user:signin')
def create_permission(request):
    if request.method == 'POST':
        form = PermissionCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PermissionCreationForm()
    return render(request, 'create_permission.html', {'form': form})

