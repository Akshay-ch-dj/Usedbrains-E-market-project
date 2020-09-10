from django.db import models
from datetime import datetime
from sellers.models import Seller


# Model Fields
class Listing(models.Model):
    '''
    Model For a item listing
    '''
    seller = models.ForeignKey(Seller, related_name='seller_listing',
                               on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255)
    # Description field set optional
    description = models.TextField(blank=True)
    price = models.IntegerField()
    item_type = models.CharField(max_length=100)  # Dropdown
    item_model = models.CharField(max_length=255)
    year = models.CharField(max_length=100)
    processor = models.CharField(max_length=255)
    gpu = models.BooleanField(default=False)
    gpu_model = models.CharField(max_length=255, blank=True)
    screen_size = models.DecimalField(max_digits=2, decimal_places=1,
                                      blank=True)
    # Extra specifications
    specifications = models.TextField(blank=True)
    item_condition = models.CharField(max_length=255)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    is_published = models.BooleanField(default=True)
    # Main photo
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    # Six thumbnail photos(optional)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    # To set the main display field in admin page
    def __str__(self):
        return self.title
