from django.contrib.auth.models import User
from djongo import models


class Currency(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=64)
    symbol = models.CharField(max_length=4)
    rate = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.title


class Account(models.Model):
    title = models.CharField(max_length=255)
    code = models.CharField(max_length=64)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    balance = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.title


class Transaction(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    currency = Currency()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    total = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    accounts = list()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)
    image = models.ImageField(default='default.jpg')

    def __str__(self):
        return self.user.username
