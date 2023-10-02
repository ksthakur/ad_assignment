from django.shortcuts import render
from app_user.models import AppUsers
from articles.models import ArticleUsers
from app_user.serializer import AppUserSerializer
from articles.serializer import ArticleSerializer
from django.shortcuts import render
import requests
from datetime import date, timedelta



from rest_framework.decorators import api_view
# Create your views here.

def home(request):
    defalut_text = 'tesla'
    if request.method == 'POST':
        user_email=request.POST.get('user_email')
        user_search_text=request.POST.get('user_search_text')
        form_user_id=request.POST.get('form_user_id')
        user_id = None
        if user_search_text == None:
            try:
                app_user = AppUsers.objects.get(email=user_email)
                user_id = app_user.id
            except AppUsers.DoesNotExist:
                name = user_email.split("@")
                user_data = {"name":name[0], "email":user_email}
                app_user_serializer = AppUserSerializer(data=user_data)
                if app_user_serializer.is_valid():
                    app_user = app_user_serializer.save()
                    user_id = app_user.id
                    #print(app_user.id)
        else:
            defalut_text = user_search_text
    today = date.today() - timedelta(days=30)
    r = requests.get('https://newsapi.org/v2/everything?q='+str(defalut_text)+'&from=2023-09-02&sortBy=publishedAt&apiKey=2e6fbc71fbeb488896e0198a9dfa0a49', params=request.GET)
    articles = []
    try:
        data = r.json()
        articles = data['articles']
    except:
        pass
    if not user_id == None:
        user_data = {"search_data":defalut_text, "search_user_id":user_id}
        article_user_serializer = ArticleSerializer(data=user_data)
        if article_user_serializer.is_valid():
            article_user = article_user_serializer.save()
            user_id = article_user.id
    context1 = {'articles' : articles, "user_id": user_id}
    return render(request, 'home_page.html', context1)
