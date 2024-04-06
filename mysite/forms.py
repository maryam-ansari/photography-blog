from django.forms import ModelForm 
from django.contrib.auth.forms import UserCreationForm
from .models import *

from django import forms
from .models import Discussion, Comment

class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = ['title','description']


"""class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'"""

class DiscussionForm(forms.ModelForm):
    class Meta:
        model = Discussion
        fields = ['title']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']