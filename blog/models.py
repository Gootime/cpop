from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.


class ListArticle(models.Model):
    name = models.CharField(max_length=16)
    article = models.ManyToManyField('Article')


class FileItem(models.Model):
    name = models.CharField(max_length=120, null=True, blank=True)
    path = models.TextField(blank=True, null=True)
    size = models.BigIntegerField(default=0)
    upload_date = models.DateTimeField(auto_now_add=True)
    file_type = models.CharField(max_length=4)
    updated = models.DateTimeField(auto_now=True)
    uploaded = models.BooleanField(default=False)


class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fileItem = models.OneToOneField('FileItem', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='static')
    category = models.ForeignKey('Category',on_delete=models.CASCADE, null=True, blank=True) #TODO
    date = models.DateTimeField(default=timezone.now, verbose_name="Date de Parution")
    slug = models.SlugField(max_length=100)
    content = models.TextField()
    adress = models.CharField(max_length=250)
    autorisation = models.BooleanField(default=True,verbose_name="Autorisation des commentaires")


class Category(models.Model):
    name = models.CharField(max_length=50)


class Commentaire(models.Model):
    pseudo = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contenu = models.TextField(null=True)
    visible = models.BooleanField(default=True)
    article = models.ForeignKey('Article',on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    def __str(self):
        return self.pseudo
        return self.email
        return self.contenu


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, blank=True)
    avatar = models.ImageField(upload_to="static",blank=True)
    favorite = models.CharField(max_length=255)

#Géoloc
