from django.urls import path

from core.views import PingView

app_name = 'core'

urlpatterns = [
	path('ping/', PingView.as_view(), name='test_view')
]
