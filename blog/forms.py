from django import forms
from .models import Article,Commentaire,Category
from froala_editor.widgets import FroalaEditor

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        exclude = ('fileItem', 'user','author')


class UserFormSignUp(forms.Form):
    pseudo = forms.CharField(max_length=60)
    adresse_mail = forms.EmailField(label="Votre adresse Email")
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=50, label="Votre prénom")
    last_name = forms.CharField(max_length=50, label="Votre nom")
    CLUF = forms.CheckboxInput()

class UserLogIn(forms.Form):
    pseudo = forms.CharField(max_length=60)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)



class CommentForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = 'pseudo','email','contenu'
