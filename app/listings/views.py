from django.shortcuts import render, get_object_or_404

from django.core.paginator import Paginator
# EmptyPage, PageNotAnInteger
from listings.models import Listing

from django.contrib.postgres.search import SearchVector
from listings.choices import price_choices, state_choices


def index(request):
    # Fetch all data from the listing table
    # Order by list date and filter out the unpublished ones.
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    # Adding pagination as per django documentation(need 6 per page)
    paginator = Paginator(listings, 6)  # 3 for testing

    page_number = request.GET.get('page')
    paged_listings = paginator.get_page(page_number)

    # Instead of listing pass paged listings
    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    # Listing id passed in through the url to the view request 'listing_id'
    single_listing = get_object_or_404(Listing, pk=listing_id)

    imgList = [f"photo_{i}" for i in range(0, 6)]
    print(imgList)

    context = {
        'listing': single_listing,
        'imgList': imgList
    }

    return render(request, 'listings/listing.html', context)


def search(request):
    '''
    View For the search items page
    filter the items from the query set
    '''
    # Grab all listings
    queryset_list = Listing.objects.order_by('-list_date')

    # The request is in the form 'search?keywords=&city=&specs='

    # The input field name is set 'keywords'
    search_vector = SearchVector('title', 'item_type', 'item_model',
                                 'processor', 'year', 'processor',
                                 'memory', 'gpu_model', 'screen_size',
                                 'list_date', 'item_condition', 'seller')

    if 'keywords' in request.GET:
        # Get only if any keywords exists.
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.annotate(
                search=search_vector).filter(search=keywords)
            # # search in the description for the item if keywords not empty.
            # queryset_list = queryset_list.filter(
            #     description__icontains=keywords)


    # For specs
    if 'specs' in request.GET:
        specs = request.GET['specs']
        if specs:
            # search in the description for the item if keywords not empty.
            queryset_list = queryset_list.filter(
                other_specifications__icontains=specs)

    context = {
        # 'spec_choices': spec_choices,
        'state_choices': state_choices,
        'price_choices': price_choices,
        'listings': queryset_list
    }

    return render(request, 'listings/search.html', context)
