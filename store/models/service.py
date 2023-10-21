from django.db import models

class Service(models.Model):
    class Meta:
        verbose_name = 'Service'
    
    name = models.CharField(max_length=50)

    @staticmethod
    def get_all_services():
        return Service.objects.all()

    def __str__(self):
        return self.name