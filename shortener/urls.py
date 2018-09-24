__author__ = 'Vladimir'

from django.urls import re_path
from shortener.views import shorten_url, redirect_to_original_url

urlpatterns = [
    re_path(r'^$', shorten_url, name="shorten_url"),
    re_path(r'^(?P<short_key>\w+)/?$', redirect_to_original_url,
            name="redirect_to_original_url"),
]
