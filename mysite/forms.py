from django.forms import ModelForm 
from django.contrib.auth.forms import UserCreationForm
from .models import *

class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = ['title','description']


"""class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'"""