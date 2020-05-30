from django.db import models
from django.contrib.auth.models import User

class Buy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_started = models.DateTimeField(auto_now=True)
    date_ended = models.DateTimeField(blank=True, null=True, default=None)
    product_link = models.URLField()
    quantity = models.PositiveIntegerField()
    price = models.DecimalField()
    


class ContribUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    buy = models.ForeignKey(User, on_delete=models.CASCADE, related_name="contribuserbuy")
    


