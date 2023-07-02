from django.contrib.auth.models import User
from django.db import models
from django.db.models import ForeignKey
from rest_framework.fields import IntegerField


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    merchant_first_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='merchant_first_name')
    merchant_last_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='merchant_last_name')
    title = models.CharField(max_length=100)
    image1 = models.ImageField()
    image2 = models.ImageField()
    image3 = models.ImageField()
    description = models.TextField()
    price = models.FloatField()
    discount_percentage = models.FloatField(blank=True, null=True)
    tax = models.FloatField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    quantity = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.product.title}"


class Like(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'

    def __str__(self):
        return self.product.title


class Card(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'

    def __str__(self):
        return self.product.title


class Order(models.Model):
    user = ForeignKey(User, on_delete=models.CASCADE)
    product = ForeignKey(Product, on_delete=models.CASCADE)
    quantity = IntegerField(default=1)
