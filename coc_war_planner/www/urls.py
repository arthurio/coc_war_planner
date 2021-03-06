from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^register/$', TemplateView.as_view(template_name='registration/register.html'), name='registration.register'),
    url(r'^login/$', TemplateView.as_view(template_name='registration/register.html'), name='registration.login'),
    url(r'^dashboard/$', TemplateView.as_view(template_name='www/dashboard.html'), name='www.dashboard'),
    url(r'^profile/$', TemplateView.as_view(template_name='www/profile.html'), name='www.profile'),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
]
