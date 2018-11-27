
from django.urls import path
from django.views.generic import TemplateView

from blog.views import views
from blog.views.file_upload import FileUploadCompleteHandler, FilePolicyAPI

urlpatterns = [

    path('', views.home, name="home"),
    path('signUp', views.signUp, name="signUp"),
    path('logIn', views.logIn, name="logIn"),
    path('logOut', views.logOut, name="logOut"),
    path('profil/<int:id>', views.profil, name="profil"),
    path('view_media', views.view_media, name="media"),
    path('post', views.post, name="post"),
    path('article/<int:id>',views.lire,name="lire"),

    # File Uploading
    path('upload', views.upload, name='upload-home'),
    path('api/files/complete/', FileUploadCompleteHandler.as_view(), name='upload-complete'),
    path('api/files/policy/', FilePolicyAPI.as_view(), name='upload-policy'),

]
