
from django.shortcuts import redirect
from django.urls import reverse


class AuthRequiredMiddleware:
	exception = ['login', ]

	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		if request