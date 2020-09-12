from django.contrib import admin

from sellers.models import Seller


class SellerAdmin(admin.ModelAdmin):
    '''
    Customize Seller table in the admin
    '''
    list_display = ('id', 'name', 'city', 'phone_number', 'email',
                    'is_authentic', 'join_date')
    list_display_links = ('id', 'name')
    list_filter = ('name',)
    list_editable = ('is_authentic',)
    list_per_page = 10
    search_fields = ('name', 'city', 'email', 'join_date')


admin.site.register(Seller, SellerAdmin)
