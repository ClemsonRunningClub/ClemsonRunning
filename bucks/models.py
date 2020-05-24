from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import  User

class Point(models.Model):
    user        = models.ForeignKey(User, unique=True, on_delete=models.CASCADE, related_name="point", null=True)
    strava_connected = models.BooleanField(null=False, default=False)
    miles         = models.DecimalField(decimal_places=1, max_digits=10000, null=True, blank=True, default=0)
    community     = models.DecimalField(decimal_places=1, max_digits=10000, null=True, blank=True, default=0)
    total         = models.DecimalField(decimal_places=1, max_digits=10000, null=True, blank=True, default=0)

    def __str__(self):
        return self.user.get_full_name()

#allows the creation of the model whenever a new user
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Point.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
