"""csf_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'api/', include('csfapi.urls'), name="csf-api"),
    path('dashboard/', TemplateView.as_view(template_name='screens/dashboard.html')),
    path('view-all-issues/', TemplateView.as_view(template_name='screens/view-all-issues.html')),
    path('view-issues-client/', TemplateView.as_view(template_name='screens/view-issues-client.html')),
    path('view-issues-clientgroup/', TemplateView.as_view(template_name='screens/view-issues-clientgroup.html')),
    path('update-issue/', TemplateView.as_view(template_name='screens/update-issue.html')),
    path('view-clients/', TemplateView.as_view(template_name='screens/view-clients.html')),
    path('update-client/', TemplateView.as_view(template_name='screens/update-client.html')),
    path('add-clientgroup/', TemplateView.as_view(template_name='screens/add-clientgroup.html')),
    path('view-clientgroup/', TemplateView.as_view(template_name='screens/view-clientgroup.html')),
    path('update-clientgroup/', TemplateView.as_view(template_name='screens/update-clientgroup.html')),
    path('view-issue/<pk>', TemplateView.as_view(template_name='screens/view-issue.html'))
]
