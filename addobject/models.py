from django.db import models
from addtype.models import *
from django import forms

class Object(models.Model):
    name = models.CharField("Бортовой номер",max_length=24)
    Types = Type.objects.all()
    type_list = Types.values_list('name','name')
    type = models.CharField("Модель",max_length=200, choices=type_list)

    max_load=models.FloatField("Максимальная грузоподъёмность")
    load=models.FloatField("Текущий вес")
    over_load=models.FloatField("Перегруз %")
