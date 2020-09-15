from django.shortcuts import render, get_object_or_404

from django.core.paginator import Paginator
# EmptyPage, PageNotAnInteger
from listings.models import Listing

# To search in multiple fields
from django.db.models import Q

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
                                 'processor', 'year', 'ram',
                                 'memory', 'gpu_model', 'screen_size',
                                 'list_date', 'item_condition', 'seller__name')

    # For a keyword
    if 'keywords' in request.GET:
        # Get only if any keywords exists.
        keywords = request.GET['keywords']
        if keywords.strip():
            queryset_list = queryset_list.annotate(
                search=search_vector).filter(search=keywords)

    # For City
    if ('city' in request.GET) and request.GET['city'].strip():
        city = request.GET['city']
        queryset_list = queryset_list.filter(
            seller__city__iexact=city
        )

    # For specs
    if ('specs' in request.GET) and request.GET['specs'].strip():
        specs = request.GET['specs']
        # search in the description for the item if keywords not empty.
        queryset_list = queryset_list.filter(
            Q(other_specifications__icontains=specs) |
            Q(description__icontains=specs) |
            Q(condition_description__icontains=specs)
            )

    # For state
    if ('state' in request.GET) and request.GET['state'].strip():
        state = request.GET['state']
        queryset_list = queryset_list.filter(
            seller__state__iexact=state
        )

    # For Price
    if ('price' in request.GET) and request.GET['price'].strip():
        price = request.GET['price']
        if price == '100000':
            queryset_list = queryset_list.filter(
                price__gte=price
            )
        else:
            queryset_list = queryset_list.filter(
                price__lte=price
            )

    context = {
        # 'spec_choices': spec_choices,
        'state_choices': state_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        'price': price
    }

    return render(request, 'listings/search.html', context)
