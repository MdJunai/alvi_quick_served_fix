from django.db import models
from .service import Service
from .customer import Customer
import datetime


class Order(models.Model):
	customer = models.ForeignKey(Customer,
								on_delete=models.CASCADE)
	service = models.ForeignKey(Service,
								on_delete=models.CASCADE)
	# quantity = models.IntegerField(default=1)
	# price = models.IntegerField()
	current_location =models.CharField(max_length=50, default='', blank=True)
	address = models.CharField(max_length=50, default='', blank=True)
	phone = models.CharField(max_length=50, default='', blank=True)
	date = models.DateField(default=datetime.datetime.today)
	status = models.BooleanField(default=False)

	def placeOrder(self):
		self.save()

	@staticmethod
	def get_orders_by_customer(customer_id):
		return Order.objects.filter(customer=customer_id).order_by('-date')
