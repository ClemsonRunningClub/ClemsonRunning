from django.db import models


class Product(models.Model):
    account_user  = models.CharField(max_length = 120)
    miles         = models.DecimalField(decimal_places=2, max_digits=10000)
    community     = models.DecimalField(decimal_places=2, max_digits=10000)
    points        = models.DecimalField(decimal_places=2, max_digits=10000)
