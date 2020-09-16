from django.shortcuts import render, redirect
from django.contrib import messages

# Views for the accounts app.


# The register View
def register(request):
    '''
    Views for the register page
    '''
    if request.method == 'POST':
        # Logic for registration
        messages.error(request, 'Testing error message')
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
