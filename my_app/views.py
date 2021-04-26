from django.shortcuts import render
from bs4 import BeautifulSoup 

# Create your views here.
def honePage(request):
    return render(request, 'base.html')

def new_search(request):
    search = request.POST.get('search')
    print(search)
    stuff_for_frontend  = {
        'search':search,

    }
    return render(request, 'my_app/new_search.html', context=stuff_for_frontend)