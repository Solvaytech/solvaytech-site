# -*- encoding: utf-8 -*-
from django.db import models
# from django.contrib.auth.models import User

class Contact(models.Model):
    name = models.CharField(max_length=300)
    subject = models.CharField(max_length=1000)
    email = models.EmailField(max_length=300)
    message = models.TextField(max_length=2500)
    date = models.DateTimeField()

    def __str__(self):
        return self.subject
    
    class Meta:
        # db_table = "Contact"
        verbose_name = "Form"
        verbose_name_plural = "Contact"

# class Order(models.Model):
#     name = models.CharField(max_length=300)
#     email = models.EmailField(max_length=300)
#     tel = models.CharField(max_length=20)
#     sirket = models.CharField(max_length=500)
#     posta = models.CharField(max_length=10)
#     sehir = models.CharField(max_length=150)
#     message = models.CharField(max_length=1005)
#     date = models.DateTimeField()

#     def __str__(self):
#         return self.name
    
#     class Meta:
#         verbose_name = "Order"
#         verbose_name_plural = "Orders"

class StajUser(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=300)
    password = models.CharField(max_length=20)
    password_regen = models.CharField(max_length=20, blank=True)
    create_date = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        # db_table = "stajDB"
        verbose_name = "User"
        verbose_name_plural = "Register"

