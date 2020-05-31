from django.db import models
from django.contrib.auth.models import User

class Buy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_started = models.DateTimeField(auto_now=True)
    date_ends = models.DateTimeField()
    product_link = models.URLField()
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=12)
    image = models.ImageField(default='default.jpg', upload_to='product_pics')
    name = models.CharField(max_length=300)
    category = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)

class Contribution(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    buy = models.ForeignKey(User, on_delete=models.CASCADE, related_name="contribuserbuy")
    quantity = models.PositiveSmallIntegerField()
     


