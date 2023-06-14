from django.db import models

# Create your models here.


class Category(models.Model):
    objects = models.Model
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Product(models.Model):
    objects = models.Model
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=200)
    product_amount = models.IntegerField()
    price = models.FloatField()
    reviews = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_image = models.ImageField(null=True, blank=True, upload_to='media')

    def __str__(self):
        return self.name


class UserCart(models.Model):
    objects = models.Model
    user_id = models.IntegerField()
    user_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_product_quantity = models.IntegerField()
    user_pr_price = models.FloatField()
    added_date = models.DateTimeField(auto_now_add=True)
