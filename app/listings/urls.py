from django.urls import path
from listings import views

urlpatterns = [
    # Listings home/index page
    path('', views.index, name='listings'),
    # For single view of listings
    path('<int:listing_id>', views.listing, name='listing'),
    # anything under listing/search
    path('search', views.search, name='search'),
]
