from django.shortcuts import render

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from listings.models import Listing


def index(request):
    # Fetch all data from the listing table
    listings = Listing.objects.all()

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
    return render(request, 'listings/listing.html')


def search(request):
    return render(request, 'listings/search.html')
