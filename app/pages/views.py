from django.shortcuts import render

# from django.core.paginator import Paginator
from listings.models import Listing
from sellers.models import Seller

from listings.choices import price_choices, state_choices


# Views for the Pages.


def index(request):
    '''
    View for the home page
    '''
    # To list out the latest 3 listings in the home page
    index_listings_list = Listing.objects.order_by('-list_date')\
        .filter(is_published=True)[:3]

    context = {
        'index_listings': index_listings_list,
        'price_choices': price_choices,
        'state_choices': state_choices
    }

    return render(request, 'pages/index.html', context)


def about(request):
    '''
    View for the about page
    '''
    # Get all realtors
    sellers_list = Seller.objects.order_by('-join_date')

    # Get MVP
    mvp_sellers = Seller.objects.all().filter(is_mvp=True)
    authentic_sellers = Seller.objects.all().filter(is_authentic=True)

    context = {
        'sellers': sellers_list,
        'mvp_sellers': mvp_sellers,
        'authentic_sellers': authentic_sellers
    }
    return render(request, 'pages/about.html', context)
