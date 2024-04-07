
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


# Create your models here.
"""
class User(AbstractUser):
    name = models.CharField(max_length=100,null=True)
    uname = models.CharField(max_length=100,null=True)
    password = models.CharField(max_length=100,null=True)
    avatar = models.ImageField(null=True,default="avatar.png")

    USERNAME_FIELD = 'uname'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name
"""
class Category(models.Model):
    
    name = models.CharField(max_length=200,null=True,blank=False)
    def __str__(self):
        return self.name

class Photo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=100,null=True,blank=False,)
    description = models.CharField(max_length=500,null=True,blank=False)
    image = models.ImageField(null=True,blank = False)
    created = models.DateTimeField(auto_now_add=True,auto_created=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

class Comments(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    #post = models.ForeignKey(Photo,on_delete=models.SET_NULL,null=True)
    post = models.CharField(max_length=100,null=True,blank=False)
    message = models.TextField(max_length=200,null=True,blank=False)
    created = models.DateTimeField(auto_now_add=True,auto_created=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.message
        
class Discussion(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=500,null=True,blank=False)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE)
    # post = models.CharField(max_length=100,null=True,blank=False)
    text = models.TextField(max_length=200,null=True,blank=False)
    created = models.DateTimeField(auto_now_add=True,auto_created=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.text



