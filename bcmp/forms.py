from django import forms
from django.contrib.auth.models import User

from .models import Comment, NewsUsers, Contact

class NewsUserForm(forms.ModelForm):
    class Meta:
        model = NewsUsers
        fields = ['name', 'email']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']
