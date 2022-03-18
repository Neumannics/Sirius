from django.shortcuts import render, redirect
from .forms import ClassCreationForm, CalendarCreationForm, NoticeCreationForm
from django.contrib.auth.decorators import login_required
from .models import Class, Notice, Event

@login_required(login_url='user:sign_in')
def create_timetable(request):
    if request.method == 'POST':
        form = ClassCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ClassCreationForm()
    return render(request, 'session/create-timetable.html', {'form': form})

@login_required(login_url='user:sign_in')
def create_calendar(request):
    if request.method == 'POST':
        form = CalendarCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CalendarCreationForm()
    return render(request, 'session/create-calendar.html', {'form': form})

@login_required(login_url='user:sign_in')
def create_notice(request):
    if request.method == 'POST':
        form = NoticeCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = NoticeCreationForm()
    return render(request, 'session/create-notice.html', {'form': form})

@login_required(login_url='user:sign_in')
def timetable(request, pk):
    classes = Class.objects.filter(team_id=pk).values('start_time', 'end_time', 'day', 'title')
    return render(request, 'session/timetable.html', {'classes': classes})

@login_required(login_url='user:sign_in')
def calendar(request, pk):
    events = Event.objects.filter(team_id=pk).values('start', 'end', 'title', 'description')
    return render(request, 'session/calendar.html', {'events': events})

@login_required(login_url='user:sign_in')
def notice_board(request, pk):
    notices = Notice.objects.filter(team_id=pk).values('title', 'description', 'created_at')
    return render(request, 'session/notice_board.html', {'notices': notices})
