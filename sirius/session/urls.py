from django.urls import path
from .views import *

app_name = 'session'

urlpatterns = [
    path('timetable/', timetable, name='timetable'),
    path('calendar/', calendar, name='calendar'),
    path('notices/', notice_board, name='notice_board'),
    path('timetable/create/', create_class, name='create_class'),
    path('event/create/', create_event, name='create_event'),
    path('notice/create', create_notice, name='create_notice'),
]