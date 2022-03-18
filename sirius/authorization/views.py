from django.shortcuts import render,redirect
from .forms import RoleCreationForm
from django.contrib.auth.decorators import login_required
from .models import Role
from team.models import Membership

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

@login_required(login_url='user:sign_in')
def show_roles(request, pk):
    members = Membership.objects.filter(team_id=pk).values('user_id__pk', 'user_id__first_name', 'user_id__last_name', 'user_id__email', 'role_id__role_name', 'role_id__role_description', 'role_id__pk')
    roles = Role.objects.filter(team_id=pk).values('pk', 'role_name', 'role_description')
    return render(request, 'show_roles.html', {'members': members, 'roles': roles})

@login_required(login_url='user:sign_in')
def update_role(request, pk):
    if request.method == 'POST':
        role = Role.objects.get(pk=pk)
        


