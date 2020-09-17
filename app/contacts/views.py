from django.shortcuts import render, redirect


def contact(request):
    '''
    View for the inquiry form
    '''
    return redirect('listings')
