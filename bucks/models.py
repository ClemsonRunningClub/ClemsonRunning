from django.db import models
from django.contrib.auth.models import User

class Point(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE, related_name="point", null=True)
    miles         = models.DecimalField(decimal_places=2, max_digits=10000, null=True, blank=True)
    community     = models.DecimalField(decimal_places=2, max_digits=10000, null=True, blank=True)
    total         = models.DecimalField(decimal_places=2, max_digits=10000, null=True, blank=True)

    def __str__(self):
        return self.user.last_name
