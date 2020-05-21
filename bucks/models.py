from django.db import models
from django.urls import reverse

class Account(models.Model):
    account_user  = models.CharField(max_length = 120)
    password      = models.CharField(max_length = 120, null=True)
    miles         = models.DecimalField(decimal_places=2, max_digits=10000, null=True, blank=True)
    community     = models.DecimalField(decimal_places=2, max_digits=10000, null=True, blank=True)
    points        = models.DecimalField(decimal_places=2, max_digits=10000, null=True, blank=True)
    email         = models.EmailField(max_length=254, default="")

    def get_absolute_urls(self):
        return reverse("Account_create", kwargs={"my_id": self.id})
