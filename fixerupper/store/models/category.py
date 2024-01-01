from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/categories', null=True)
    parent_category = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE,related_name='subcategories')
    
    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    @staticmethod
    def get_parent_categories():
        return Category.objects.filter(parent_category__isnull=True)

    def __str__(self):
        return self.name
    