from django.urls import path

from core.views import GetSelfUserView

app_name = 'core'

urlpatterns = [
	path('get_self/', GetSelfUserView.as_view(), name='get_self_user_view')
]
