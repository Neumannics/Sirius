from django.shortcuts import render,redirect
from .forms import RoleCreationForm
from django.contrib.auth.decorators import login_required
from .models import Role
from authorization.models import Membership
from sirius.utils.perm import hasPerm
from django.http import HttpResponseForbidden
from sirius.utils.console_context import get_console_data

@login_required(login_url='user:signin')
def create_role(request, team):
    if request.method == 'POST':
        if not hasPerm('C', 'R', request.user, team):
            return HttpResponseForbidden()
        form = RoleCreationForm(request.POST)
        if form.is_valid():
            form.instance.team_id = team
            form.save()
            return redirect('/')
    else:
        form = RoleCreationForm()
    return render(request, 'create_role.html', {'form': form, 'console': get_console_data(team, request.user)})

@login_required(login_url='user:signin')
def show_roles(request, pk):
    if not hasPerm('R', 'R', request.user, pk):
        return HttpResponseForbidden()
    members = Membership.objects.filter(team_id=pk).values('user_id__pk', 'user_id__first_name', 'user_id__last_name', 'user_id__email', 'role_id__role_name', 'role_id__role_description', 'role_id__pk')
    roles = Role.objects.filter(team_id=pk).values('pk', 'role_name', 'role_description')
    return render(request, 'show_roles.html', {'members': members, 'roles': roles, 'console': get_console_data(pk, request.user)})

@login_required(login_url='user:signin')
def update_role(request, pk):
    if request.method == 'POST':
        if not hasPerm('U', 'R', request.user, pk):
            return HttpResponseForbidden()
        role = Role.objects.get(pk=pk)
        form = RoleCreationForm(request.POST, instance=role)
        if form.is_valid():
            form.save()
            return redirect('authorization:show_roles', pk=pk)
        


