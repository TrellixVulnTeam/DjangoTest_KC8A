from django.db import models


class Type(models.Model):
    name = models.CharField('Модель машины',max_length=24)
