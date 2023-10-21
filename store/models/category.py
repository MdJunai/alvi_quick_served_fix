from django.db import models

class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
    
    name = models.CharField(max_length=50)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name
