from django.urls import path
from contacts import views

urlpatterns = [
    # Listings home/index page
    path('contact', views.contact, name='contact')
]
