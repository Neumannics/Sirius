from django.urls import path
from .views import *

app_name = 'team'

urlpatterns = [
    path('create/', create_team, name='create_team'),
    path('<pk>/create/', create_team, name='create_sub_team'),
    path('<pk>/', team_info, name='team_info'),
    path('<pk>/send-invite/<user>/', send_invite, name='send_invite'),
    path('<pk>/send-join-request/', send_join_request, name='send_join_request'),
    path('<pk>/invites/', invites, name='invites'),
    path('<pk>/join-requests/', join_requests, name='join_requests'),
    path('accept-invite/<pk>/', accept_invite, name='accept_invite'),
    path('accept-join-request/<pk>/', accept_join_request, name='accept_join_request'),
    path('decline-invite/<pk>/', decline_invite, name='decline_invite'),
    path('decline-join-request/<pk>/', decline_join_request, name='decline_join_request'),
]