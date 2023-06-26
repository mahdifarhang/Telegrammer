from django.urls import path

from core.views import *

app_name = 'core'

urlpatterns = [
	path('ping/', test_view, name='test_view')
]
