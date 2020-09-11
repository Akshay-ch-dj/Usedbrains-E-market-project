from django.db import models
from datetime import datetime


class Seller(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)
    # Should have one photo
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    email = models.EmailField(max_length=255, unique=True)
    is_authentic = models.BooleanField(default=False)
    join_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
