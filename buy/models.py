from django.db import models
from django.contrib.auth.models import User

class Buy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_started = models.DateTimeField(auto_now=True)
    date_ended = models.DateTimeField(blank=True, null=True, default=None)
    product_link = models.URLField()
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=12)
    image = models.ImageField(default='default.jpg', upload_to='product_pics')

class Contribution(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    buy = models.ForeignKey(User, on_delete=models.CASCADE, related_name="contribuserbuy")
    quantity = models.PositiveSmallIntegerField()
    


