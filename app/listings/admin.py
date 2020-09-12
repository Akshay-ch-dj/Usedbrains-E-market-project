from django.contrib import admin

from listings.models import Listing


# To edit the admin area
class ListingAdmin(admin.ModelAdmin):
    '''
    Customizing the admin panel display items
    '''
    list_display = ('id', 'title', 'is_published', 'price', 'list_date',
                    'seller')
    # Set the title also to be link
    list_display_links = ('id', 'title')

    # To add a filter by realtors
    list_filter = ('seller',)

    # Make the 'is_published' boolean clickable
    list_editable = ('is_published',)

    # Can add search fields
    search_fields = ('title', 'description', 'year', 'processor',
                     'graphics_type', 'memory', 'price')

    # Amount of listings per page
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)
