from django.shortcuts import render
from django.template import loader
import requests
from django.urls import reverse
from django.shortcuts import render,HttpResponse, HttpResponseRedirect,redirect

# API_KEY = '062bacedde7648bba75aa82211cad03d'
# API_KEY = '5a506e349dcd42a3b996ec04f8a6105d'
API_KEY= 'c41caf728db046c8a4acfb7883864b34'
# Create your views here.
def refresh_data(request):
       url = f'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={API_KEY}'
       response = requests.get(url)
       data = response.json()
       articles = data['articles']
   
    
       return redirect('index')

def index(request):

    country = request.GET.get('country')
    category = request.GET.get('category')
    description = request.GET.get('description')
    publishedAt = request.GET.get('publishedAt')
    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']

    elif category:
        url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    elif description :
        url = f'https://newsapi.org/v2/top-headlines?q={description}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    elif publishedAt :
        url = f'https://newsapi.org/v2/top-headlines?q=2023&from={publishedAt}&sortBy=publishedAt&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    else:
        url = f'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    # url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']
    context = {
       "articles":articles,
        }


    temp = loader.get_template('index.html')  
    return HttpResponse(temp.render(context,request))

   
