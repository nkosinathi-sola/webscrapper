import requests
from django.shortcuts import render
from bs4 import BeautifulSoup

# Create your views here.
def home(request):
    return render(request, 'base.html')


def new_search(request):
    # to pull out whats searched - get is get as in pull from
    search = request.POST.get('search')
    print(search)
    # this sends the results to front end
    stuff_for_frontend = {
        'search': search,
    }
    return render(request, 'new_search.html', stuff_for_frontend)
