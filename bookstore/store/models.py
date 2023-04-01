from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name

    class Meta:
        db_table = 'app_categories'

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    image = models.FileField(null=True, blank=True, upload_to="books/")
    quantity = models.IntegerField()
    
    class Meta:
        db_table = 'app_books'