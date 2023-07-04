from django.urls import path

from core import views

app_name = 'core'

urlpatterns = [
	path('get_self/', views.GetSelfUserView.as_view(), name='get_self_user_view'),
	path('get_projects/', views.GetUserProjects.as_view(), name='get_self_projects_view'),
]
