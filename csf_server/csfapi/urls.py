from django.urls import path, include
from csfapi.views import issues_view, issues_view_details, users_view, clients_view, clients_view_details, clientgroups_view, clientgroups_view_details, userlogin_view

urlpatterns = [
    path(r'issues/', issues_view, name='issues_view'),
    path(r'issues/<pk>', issues_view_details, name='issues_view_details'),
    path(r'users/', users_view, name='users_view'),
    path(r'clients/', clients_view, name='client_view'),
    path(r'clients/<pk>', clients_view_details, name='clients_view_details'),
    path(r'clientgroups/', clientgroups_view, name='clientgroups_view'),
    path(r'clientgroups/<pk>', clientgroups_view_details, name='clientgroups_view_details'),
    path(r'userlogin/', userlogin_view, name='userlogin_view'),
]
