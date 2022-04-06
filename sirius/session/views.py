from django.shortcuts import render, redirect
from .forms import ClassCreationForm, CalendarCreationForm, NoticeCreationForm
from django.contrib.auth.decorators import login_required
from .models import Class, Notice, Event
from authorization.models import Membership, Permission, Role
from django.http import HttpResponseForbidden
from sirius.utils.perm import hasPerm


@login_required(login_url='user:sign_in')
def create_timetable(request):
    if request.method == 'POST':
        form = ClassCreationForm(request.POST)
        if form.is_valid():
            if form.cleaned_data.get('parent_id'):
                if not hasPerm('C', 'S', request.user, form.cleaned_data.get('parent_id')):
                    return HttpResponseForbidden()
            form.save()
            return redirect('session:timetable', pk=form.instance.pk)
    else:
        form = ClassCreationForm()
    return render(request, 'session/create-timetable.html', {'form': form})

@login_required(login_url='user:sign_in')
def create_calendar(request):
    if request.method == 'POST':
        form = CalendarCreationForm(request.POST)
        if form.is_valid():
            if form.cleaned_data.get('parent_id'):
                if not hasPerm('C', 'S', request.user, form.cleaned_data.get('parent_id')):
                    return HttpResponseForbidden()
            form.save()
            return redirect('session:calendar', pk=form.instance.pk)
    else:
        form = CalendarCreationForm()
    return render(request, 'session/create-calendar.html', {'form': form})

@login_required(login_url='user:sign_in')
def create_notice(request):
    if request.method == 'POST':
        form = NoticeCreationForm(request.POST)
        if form.is_valid():
            form.save()
            if form.cleaned_data.get('parent_id'):
                if not hasPerm('C', 'S', request.user, form.cleaned_data.get('parent_id')):
                    return HttpResponseForbidden()
            return redirect('session:notice', pk=form.instance.pk)
    else:
        form = NoticeCreationForm()
    return render(request, 'session/create-notice.html', {'form': form})

@login_required(login_url='user:sign_in')
def timetable(request, pk):
    if not hasPerm('R', 'S', request.user, pk):
        return HttpResponseForbidden()
    classes = Class.objects.filter(team_id=pk).values('start_time', 'end_time', 'day', 'title')
    return render(request, 'session/timetable.html', {'classes': classes})

@login_required(login_url='user:sign_in')
def calendar(request, pk):
    if not hasPerm('R', 'S', request.user, pk):
        return HttpResponseForbidden()
    events = Event.objects.filter(team_id=pk).values('start', 'end', 'title', 'description')
    return render(request, 'session/calendar.html', {'events': events})

@login_required(login_url='user:sign_in')
def notice_board(request, pk):
    if not hasPerm('R', 'S', request.user, pk):
        return HttpResponseForbidden()
    notices = Notice.objects.filter(team_id=pk).values('title', 'description', 'created_at')
    return render(request, 'session/notice_board.html', {'notices': notices})
