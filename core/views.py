from django.shortcuts import render
from django.http.response import JsonResponse


# Create your views here.

def test_view(request):
	return JsonResponse({
		'pong': True,
		'status': 'OK',
	}, status=200)
