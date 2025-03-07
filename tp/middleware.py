
from django.shortcuts import redirect
from django.urls import reverse


class AuthRequiredMiddleware:
	# exception = ['login', ]

	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		username = request.POST.get('username')
		login_path = reverse('login')

		# if request.path != login_path:			
		print(username)
		if username != 'admin':
			# return redirect(login_path)
			pass

		return self.get_response(request)