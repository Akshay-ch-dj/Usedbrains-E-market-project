from django.shortcuts import redirect
from django.contrib import messages

from contacts.models import Contact


def contact(request):
    '''
    View for the inquiry form
    '''
    if request.method == 'POST':
        # The data that are get posted from the form: user_id, seller_email
        # listing_id, listing(title), name(user), email, phone, message
        listing_id = request.POST['listing_id']
        user_id = request.POST['user_id']
        seller_email = request.POST['seller_email']
        listing_title = request.POST['listing_title']
        user_name = request.POST['name']
        user_email = request.POST['email']
        user_phone = request.POST['phone']
        user_message = request.POST['message']

        contact = Contact(listing=listing_title,
                          listing_id=listing_id,
                          name=user_name,
                          email=user_email,
                          phone=user_phone,
                          message=user_message,
                          user_id=user_id)

        contact.save()

        messages.success(request, "Your interest recorded, the seller will \
            get back to you soon")
        return redirect(f'/listings/{listing_id}')
