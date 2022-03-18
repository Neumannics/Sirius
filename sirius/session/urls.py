from django.urls import path
from .views import *

app_name = 'session'

urlpatterns = [
    path('create_timetaable/', create_timetable, name='create_timetable'),
    path('create_calendar/', create_calendar, name='create_calendar'),
    path('create_notice/', create_notice, name='create_notice'),
    path('timetable/<pk>/', timetable, name='timetable'),
    path('calendar/<pk>/', calendar, name='calendar'),
    path('notice_board/<pk>/', notice_board, name='notice_board'),
]