"""
agid_template URL Configuration
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import *

app_name="django_unical_bootstrap_italia"

urlpatterns = [
    path('', index, name='index'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
