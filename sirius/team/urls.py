from django.urls import path
from .views import *

app_name = 'team'

urlpatterns = [
    path('create/', create_team, name='create_team'),
    path('<pk>/', team_info, name='team_info'),
    path('<pk>/send_invite/<user>/', send_invite, name='send_invite'),
    path('<pk>/send_join_request/', send_join_request, name='send_join_request'),
    path('<pk>/invites/', invites, name='invites'),
    path('<pk>/join_requests/', join_requests, name='join_requests'),
    path('accept_invite/<pk>/', accept_invite, name='accept_invite'),
    path('accept_join_request/<pk>/', accept_join_request, name='accept_join_request'),
    path('decline_invite/<pk>/', decline_invite, name='decline_invite'),
    path('decline_join_request/<pk>/', decline_join_request, name='decline_join_request'),
]