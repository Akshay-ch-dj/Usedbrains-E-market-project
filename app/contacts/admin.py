from django.contrib import admin

from contacts.models import Contact


class ContactAdmin(admin.ModelAdmin):
    '''
    Customize the model in admin page
    '''
    list_display = ('id', 'name', 'listing', 'email', 'contact_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'listing')
    list_per_page = 25


admin.site.register(Contact, ContactAdmin)