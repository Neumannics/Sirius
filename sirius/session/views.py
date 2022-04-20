from django.shortcuts import render, redirect
from .forms import ClassCreationForm, CalendarCreationForm, NoticeCreationForm
from django.contrib.auth.decorators import login_required
from .models import Class, Notice, Event
from authorization.models import Membership, Permission, Role
from django.http import HttpResponseForbidden
from sirius.utils.perm import has_perm
from sirius.utils.console_context import get_console_data
from team.models import Team


@login_required(login_url='user:signin')
def create_class(request, pk):
    if request.method == 'POST':
        form = ClassCreationForm(request.POST)
        if form.is_valid() and pk:
            if not has_perm('C', 'C', request.user, pk):
                return HttpResponseForbidden()
            new_class = form.save(commit=False)
            new_class.team_id = pk
            new_class.save()
            return redirect('session:timetable', pk=pk)
    else:
        form = ClassCreationForm()
    return render(request, 'create_class.html', {'form': form, 'console': get_console_data(pk, request.user)})

@login_required(login_url='user:signin')
def create_event(request, pk):
    if request.method == 'POST':
        form = CalendarCreationForm(request.POST)
        if form.is_valid() and pk:
            if not has_perm('C', 'E', request.user, pk):
                return HttpResponseForbidden()
            new_event = form.save(commit=False)
            new_event.team_id = pk
            new_event.save()
            return redirect('session:calendar', pk=pk)
    else:
        form = CalendarCreationForm()
    return render(request, 'create_event.html', {'form': form, 'console': get_console_data(pk, request.user)})

@login_required(login_url='user:signin')
def create_notice(request, pk):
    if request.method == 'POST':
        form = NoticeCreationForm(request.POST)
        if form.is_valid() and pk:
            if not has_perm('C', 'N', request.user, pk):
                return HttpResponseForbidden()
            new_notice = form.save(commit=False)
            new_notice.team_id = pk
            new_notice.save()
            return redirect('session:notice', pk=pk)
    else:
        form = NoticeCreationForm()
    return render(request, 'create_notice.html', {'form': form, 'console': get_console_data(pk, request.user)})

@login_required(login_url='user:signin')
def timetable(request, pk):
    if not has_perm('R', 'C', request.user, pk):
        return HttpResponseForbidden()
    classes = Class.objects.filter(team_id=pk).values('start_time', 'end_time', 'day', 'title')
    # team = Team.objects.get(pk=pk)
    return render(request, 'timetable.html', {'classes': classes, 'console': get_console_data(pk, request.user)})

@login_required(login_url='user:signin')
def calendar(request, pk):
    if not has_perm('R', 'E', request.user, pk):
        return HttpResponseForbidden()
    events = Event.objects.filter(team_id=pk).values('start', 'end', 'title', 'description')
    return render(request, 'calendar.html', {'events': events, 'console': get_console_data(pk, request.user)})

@login_required(login_url='user:signin')
def notice_board(request, pk):
    if not has_perm('R', 'N', request.user, pk):
        return HttpResponseForbidden()
    notices = Notice.objects.filter(team_id=pk).values('title', 'description', 'created_at')
    return render(request, 'notice_board.html', {'notices': notices, 'console': get_console_data(pk, request.user)})
