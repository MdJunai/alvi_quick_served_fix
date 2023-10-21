from django.db import models
from .category import Category

class Partner(models.Model):
    class Meta:
        verbose_name = 'Partner'
    
    partner_name = models.CharField(max_length=50)
    workshop_name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    mobile = models.CharField(max_length=10)
    locality = models.CharField(max_length=50)
    # email = models.EmailField()
    # password = models.CharField(max_length=100)

    @staticmethod
    def get_all_partners():
        return Partner.objects.all()
    
    @staticmethod
    def get_partner_by_id(ids):
        return Partner.objects.filter(id__in=ids)
    @staticmethod
    def get_all_partner_by_categoryid(category_id):
           if category_id:
            return Partner.objects.filter(category=category_id)
           else:
               return Partner.get_all_products()

    def __str__(self):
        return self.workshop_name