from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.models import Article, Commentaire, Category, FileItem
from django.urls import reverse
from blog.forms import UserLogIn, UserFormSignUp, ArticleForm, CommentForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import urllib
import json



def home(request):
    articles = Article.objects.all()
    allArticle = Article.objects.all()
    listMarker = []
    for article in allArticle:
        listMarker.append((getLatLng(article.adress),article.title))
    print(listMarker,allArticle)
    return render(request, 'blog/home.html', locals())

def lire(request,id):
    oneArticle = Article.objects.get(id=id)
    center = getLatLng(oneArticle.adress)
    getCat=Category.objects.get(id=oneArticle.category_id)
    allArticle = []
    listMarker = []
    for article in allArticle:
        listMarker.append((getLatLng(article.adress),article.title))

    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.visible = True
        contenu = form.cleaned_data['contenu']
        comment.article=oneArticle
        comment.save()
    Comment = Commentaire.objects.filter(article_id=oneArticle.id)
    return render(request,'blog/oneArticle.html', locals())


def logIn(request):
    error=False
    form = UserLogIn(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['pseudo']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            error=True

    return render(request, 'blog/logIn.html', locals())

def logOut(request):
    logout(request)
    return redirect('home')


def signUp(request):
    error=False
    form = UserFormSignUp(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        user = User.objects.create_user(
            username=data['pseudo'],
            email=data['adresse_mail'],
            password=data['password'],
            first_name=data['first_name'],
            last_name=data['last_name'])
        user.save()
        auth = authenticate(username=data['pseudo'], password=data['password'])
        if auth :
            login(request,auth)
            return redirect('home')
        else:
            error=True
    return render(request, 'blog/signUp.html', locals())

@login_required
def profil(request,id):
    UserProfil=User.objects.get(id=id)
    return render(request, 'blog/profil.html', locals())



def view_media(request):
    items = FileItem.objects.all()
    itemsVideo = [i for i in items if i.name.split('.')[-1] == 'mp4']

    itemsImage = [i for i in items if i.name.split('.')[-1] != 'mp4']
    return render(request, 'blog/view_media.html', locals())

@login_required
def upload(request):
    form = ArticleForm()
    return render(request, 'blog/upload/upload.html', locals())

def getLatLng(adresse):
    googleGeocodeUrl = 'https://maps.googleapis.com/maps/api/geocode/json?'
    query = adresse.encode('utf-8')
    params = {
        'address': query,
        'sensor': "true"
    }
    url = googleGeocodeUrl + urllib.parse.urlencode(params) + "&key=AIzaSyDSyghpSVaeCKCEa80aGrXCl4rUwZVfea8"
    json_response = urllib.request.urlopen(url)
    response = json.loads(json_response.read())
    print(response['results'][0]['geometry']['location'])
    if response['results']:
        location = response['results'][0]['geometry']['location']
        latitude = location['lat']
        longitude = location['lng']
    else:
        latitude, longitude = None, None

    return latitude , longitude

@login_required
def post(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.fileItem_id = request.POST['id_file']
            article.save()
        else:
            print(form.errors)
    return view_media(request)
