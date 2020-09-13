from django.shortcuts import render

from django.core.paginator import Paginator
from listings.models import Listing

# Views for the Pages.


def index(request):
    '''
    View for the home page
    '''
    # To list out the latest 3 listings in the home page
    index_listings_list = Listing.objects.order_by('-list_date')\
        .filter(is_published=True)[:3]

    context = {
        'index_listings': index_listings_list
    }

    return render(request, 'pages/index.html', context)


def about(request):
    return render(request, 'pages/about.html')
