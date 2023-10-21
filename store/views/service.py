from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from store.models.service import Service
from django.views import View


class Services(View):
	return_url = None

	def get(self, request):
		Services.return_url = request.GET.get('return_url')
		ids = list(request.session.get('cart').keys())
		
		services = Service.get_all_services()
		print(services)
		return render(request, 'service.html',{'services' : services})