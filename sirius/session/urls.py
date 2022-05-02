from django.urls import path
from .views import *

app_name = 'session'

urlpatterns = [
    path('timetable/', timetable, name='timetable'),
    path('calendar/', calendar, name='calendar'),
    path('notices/', notice_board, name='notice_board'),
    path('class/create/', create_class, name='create_class'),
    path('event/create/', create_event, name='create_event'),
    path('notice/create', create_notice, name='create_notice'),
    path('notice/update/<int:n_pk>', update_notice, name='update_notice'),
    path('event/update/<int:e_pk>', update_event, name='update_event'),
    path('class/update/<int:c_pk>', update_class, name='update_class'),
]