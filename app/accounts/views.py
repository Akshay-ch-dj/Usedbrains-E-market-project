from django.shortcuts import render, redirect
from django.contrib import messages

# Default Django User model
from django.contrib.auth.models import User

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
        # Logic for login
        pass
    else:
        return render(request, 'accounts/login.html')


# For the logout page
def logout(request):
    '''
    Views for the logout page
    '''

    # redirect the user back to the index page.
    return redirect('index')


# For the dashboard page
def dashboard(request):
    '''
    Views for the dashboard page
    '''
    return render(request, 'accounts/dashboard.html')
