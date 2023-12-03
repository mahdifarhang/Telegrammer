from django.urls import path

from core import views

app_name = 'core'

urlpatterns = [
	path('get-self/', views.GetSelfUserView.as_view(), name='get_self_user_view'),
	path('get-projects/', views.GetUserProjects.as_view(), name='get_self_projects_view'),
	path('get-bots/', views.GetUserTelegramBots.as_view(), name='get_self_telegram_bots_view'),
]
