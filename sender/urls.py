from django.urls import path

from sender import views

app_name = 'sender'

urlpatterns = [
	path('send-message/', views.SendMessage.as_view(), name='send_message'),
	path('get-message/<int:pk>/', views.GetMessage.as_view(), name='get_message'),
]
