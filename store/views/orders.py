from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.models.products import Products
from store.models.orders import Order
from store.middlewares.auth import auth_middleware


class OrderView(View):

	def get(self, request):
		customer = request.session.get('customer')
		orders = Order.get_orders_by_customer(customer)
		print(orders)
		return render(request, 'orders.html', {'orders': orders})
	
	def post(self, request):
		name=request.POST.get('name')
		location=request.POST.get('location')
		phone=request.POST.get('phone')
		service = request.POST.get('service')
		# password = request.POST.get('password')
		workshop_name = request.POST.get('workshop_name')
		contact_namuber = request.POST.get('contact_namuber')
		# customer = Customer.get_customer_by_email(email)
		error_message = None
		# if customer:
		# 	flag = check_password(password, customer.password)
		# 	if flag:
		# 		request.session['customer'] = customer.id

		# 		if Login.return_url:
		# 			return HttpResponseRedirect(Login.return_url)
		# 		else:
		# 			Login.return_url = None
		# 			return redirect('homepage')
		# 	else:
		# 		error_message = 'Invalid !!'
		# else:
		# 	error_message = 'Invalid !!'
		# order = Order(customer=Customer(id=customer),
		# 				product=product,
		# 				price=product.price,
		# 				address=address,
		# 				phone=phone,
		# 				quantity=cart.get(str(product.id)))
		# 	order.save()

		print(name, phone)
		return render(request, 'login.html', {'error': error_message})

