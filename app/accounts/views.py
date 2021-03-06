from django.shortcuts import render, redirect
from django.contrib import messages, auth

# Default Django User model
from django.contrib.auth.models import User
from contacts.models import Contact

# Views for the accounts app.


# The register View
def register(request):
    '''
    Views for the register page
    '''
    if request.method == 'POST':
        # Get the form submitted data using "name" tag
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Logic for registration
        # Check if passwords match
        if password == password2:
            # Check duplicate usernames
            if User.objects.filter(username=username).exists():
                # Show Error there is already a User in with that name.
                messages.error(request, 'Username exists, please give another \
                    one')
                return redirect('register')
            else:
                # Check for the email
                if User.objects.filter(email=email).exists():
                    # Show Error there is already a User in with that name.
                    messages.error(request, 'Email is being used')
                    return redirect('register')
                else:
                    # Looks Good, Can register the User
                    user = User.objects.create_user(
                        username=username,
                        password=password,
                        email=email,
                        first_name=first_name,
                        last_name=last_name
                        )

                    # Redirect to login page
                    user.save()
                    messages.success(request, 'Registration Completed \
                        redirecting to login page')
                    return redirect('login')
        else:
            # Error message
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


# For the login page
def login(request):
    '''
    Views for the login page
    '''
    if request.method == 'POST':
        # Accept the username and password
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        # If user is found & matched in the database
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


# For the logout page
def logout(request):
    '''
    Views for the logout page
    '''
    if request.method == 'POST':
        auth.logout(request)
        # Message
        messages.success(request, 'You are now successfully logged out')
        # redirect the user back to the index page.
        return redirect('index')


# For the dashboard page
def dashboard(request):
    '''
    Views for the dashboard page
    '''
    # Get the contact made by the current user
    user_contacts = Contact.objects.order_by('-contact_date').filter(
        user_id=request.user.id)

    context = {
        'contacts': user_contacts
    }
    return render(request, 'accounts/dashboard.html', context)
