from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.http import HttpResponseForbidden

from team.models import Team, JoinRequest, Invite
from .forms import TeamCreationForm, JoinRequestForm
from authorization.models import Membership, Permission, Role
from sirius.utils.perm import getPerms, hasPerm
from sirius.utils.console_context import get_console_data

@login_required(login_url='user:signin')
def create_team(request, pk=None):
    if request.method == 'POST':
        form = TeamCreationForm(request.POST)
        if form.is_valid():
            team = form.save(commit=False)
            if pk is not None:
                if Team.objects.filter(pk=pk).count() == 0:
                    raise form.ValidationError('Parent team does not exist')
                if not hasPerm('C', 'T', request.user, pk):
                    return HttpResponseForbidden()
                else:
                    team.parent_id = pk
            team.save()
            admin_role = Role.objects.create(role_name='Admin', team_id=form.instance, role_description='Admin')
            admin_permission = Permission.objects.all().values('pk')
            permission_string = ""
            for permission in admin_permission:
                permission_string += str(permission['pk']) + ","
            admin_role.permissions = permission_string
            admin_role.save()
            Role.objects.create(role_name='Member', team_id=form.instance, role_description='Member of the team')
            Membership.objects.create(user_id=request.user, team_id=form.instance, role_id=admin_role)
            return redirect('team:team_info', pk=form.instance.pk)
    else:
        form = TeamCreationForm()
        if pk is not None:
            team = Team.objects.get(pk=pk)
            if team:
                render(request, 'new_team.html', {'form': form, 'console': get_console_data(pk, request.user)})
        return render(request, 'new_team.html', {'form': form})

# @login_required(login_url='user:signin')
# def create_sub_team(request, pk):
#     if request.method == 'POST':
#         form = TeamCreationForm(request.POST)
#         if form.is_valid():
#             if form.cleaned_data.get('parent_id'):
#                 if not hasPerm('C', 'T', request.user, form.cleaned_data.get('parent_id')):
#                     return HttpResponseForbidden()
#             form.save()
#             admin_role = Role.objects.create(role_name='Admin', team_id=form.instance, role_description='Admin of the team')
#             admin_permission = Permission.objects.all().values('pk')
#             permission_string = ""
#             for permission in admin_permission:
#                 permission_string += str(permission['pk']) + ","
#             admin_role.permissions = permission_string
#             admin_role.save()
#             Role.objects.create(role_name='Member', team_id=form.instance, role_description='Member of the team')
#             Membership.objects.create(user_id=request.user, team_id=form.instance, role_id=admin_role)
#             return redirect('team:team_info', pk=form.instance.pk)
#     else:
#         return render(request, 'new_team.html', {'form': TeamCreationForm()})

@login_required(login_url='user:signin')
def team_info(request, pk):
    parents = []
    team = Team.objects.get(pk=pk)
    temp = team.parent_id
    while temp != None:
        parents.append(Team.objects.values('name', 'pk').get(pk=temp))
        temp = temp.parent_id
    members = Membership.objects.filter(team_id=pk).values('created_at', 'alumni', 'user_id__pk', 'user_id__first_name', 'user_id__last_name', 'user_id__username', 'role_id__pk', 'role_id__role_name')
    children = Team.objects.filter(parent_id=pk).values('name', 'pk')
    return render(request, 'team_info.html', {'members': members, 'children': children, 'console': get_console_data(pk, request.user)})

@login_required(login_url='user:signin')
def send_invite(request, pk, user):
    if request.method == 'POST':
        if not hasPerm('C', 'I', request.user, pk):
            return HttpResponseForbidden()
        if Invite.objects.filter(status = 'P', team_id=pk, invited=user).exists():
            return redirect('team:team_info', pk=pk)
        invite = Invite(team_id=Team.objects.get(pk=pk), created_by=request.user, invited=get_user_model().objects.get(pk=user))
        invite.save()
        return redirect('team:team_info', pk=pk)
    return redirect('team:team_info', pk=pk)

@login_required(login_url='user:signin')
def send_join_request(request):
    if request.method == 'POST':
        form = JoinRequestForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            request.session['join_form_errors'] = form.errors
            return redirect('user:dashboard', u_pk=request.user.pk)
    return redirect('user:dashboard', u_pk=request.user.pk)

@login_required(login_url='user:signin')
def invites(request, pk):
    if not hasPerm('R', 'I', request.user, pk):
        return HttpResponseForbidden()
    invites = Invite.objects.filter(team_id=pk, status='P').values('invited__first_name', 'invited__last_name', 'invited__email', 'invited__pk', 'created_at', 'status', 'pk', 'created_by__first_name', 'created_by__last_name', 'created_by__email', 'created_by__pk')
    return render(request, 'invites.html', {'invites': invites, 'console': get_console_data(pk, request.user)})

@login_required(login_url='user:signin')
def join_requests(request, pk):
    if not hasPerm('R', 'JR', request.user, pk):
        return HttpResponseForbidden()
    requests = JoinRequest.objects.filter(team_id=pk, status='P').values('user_id__first_name', 'user_id__last_name', 'user_id__username', 'user_id__pk', 'created_at', 'status', 'pk')
    return render(request, 'join_requests.html', {'requests': requests, 'console': get_console_data(pk, request.user)})

@login_required(login_url='user:signin')
def accept_invite(request, pk):
    if request.method == 'POST':
        invite = Invite.objects.get(pk=pk)
        if not hasPerm('U', 'I', request.user, invite.team_id.pk):
            return HttpResponseForbidden()
        invite.status = 'A'
        invite.save()
        membership = Membership(team_id=invite.team_id, user_id=invite.invited)
        membership.save()
        return redirect('team:team_info', pk=invite.team_id.pk)

@login_required(login_url='user:signin')
def accept_join_request(request, pk):
    if request.method == 'POST':
        join_request = JoinRequest.objects.get(pk=pk)
        if not hasPerm('U', 'JR', request.user, join_request.team_id.pk):
            return HttpResponseForbidden()
        join_request.status = 'A'
        join_request.save()
        membership = Membership(team_id=join_request.team_id, user_id=join_request.user_id)
        membership.save()
        return redirect('team:team_info', pk=request.team_id.pk)

@login_required(login_url='user:signin')
def decline_invite(request, pk):
    if request.method == 'POST':
        invite = Invite.objects.get(pk=pk)
        if not hasPerm('U', 'I', request.user, invite.team_id.pk):
            return HttpResponseForbidden()
        invite.status = 'R'
        invite.save()
        return redirect('user:dashboard', pk=invite.team_id.pk)

@login_required(login_url='user:signin')
def decline_join_request(request, pk):
    if request.method == 'POST':
        join_request = JoinRequest.objects.get(pk=pk)
        if not hasPerm('U', 'JR', request.user, join_request.team_id.pk):
            return HttpResponseForbidden()
        join_request.status = 'R'
        join_request.save()
        return redirect('user:dashboard', pk=join_request.team_id.pk)

@login_required(login_url='user:signin')
def leave_team(request, pk):
    if request.method == 'POST':
        membership = Membership.objects.get(user_id=request.user.pk, team_id=pk)
        membership.delete()
        return redirect('user:dashboard', pk=pk)

@login_required(login_url='user:signin')
def permissions(request, pk):
    if not hasPerm('R', 'P', request.user, pk):
        return HttpResponseForbidden()
    perms = Permission.objects.filter(team_id=pk).values('user_id__first_name', 'user_id__last_name', 'user_id__pk', 'team_id__name', 'team_id__pk', 'permission_name', 'pk')
    return render(request, 'permissions.html', {'perms': perms, 'console': get_console_data(pk, request.user)})
