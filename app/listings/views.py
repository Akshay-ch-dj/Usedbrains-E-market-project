from django.shortcuts import render, get_object_or_404

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from listings.models import Listing


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
    return render(request, 'listings/search.html')
