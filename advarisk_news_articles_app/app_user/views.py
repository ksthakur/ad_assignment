from django.http import HttpResponse
from django.shortcuts import render
from app_user.models import AppUsers
from app_user.serializer import AppUserSerializer
from django.shortcuts import render
import requests
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from rest_framework.decorators import api_view
# Create your views here.


def index(request):
    return render(request, "select_user.html")

#def home(request):
    #context1 = {'users' : AppUsers.objects.filter(is_active=True)}
    #r = requests.get('https://newsapi.org/v2/everything?q=tesla&from=2023-09-01&sortBy=publishedAt&apiKey=2e6fbc71fbeb488896e0198a9dfa0a49', params=request.GET)
    #data = r.json()
    #print(data['articles'][0])
    #return render(request, 'home_page.html', context1)
