from django.shortcuts import render, redirect

# Views for the accounts app.


# The register View
def register(request):
    '''
    Views for the register page
    '''
    return render(request, 'accounts/register.html')


# For the login page
def login(request):
    '''
    Views for the login page
    '''
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
