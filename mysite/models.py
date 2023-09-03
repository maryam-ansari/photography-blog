from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=200,null=True,blank=False)
    #user = models.ForeignKey(User,on_delete=CASCADE)
    def __str__(self):
        return self.name

class Photo(models.Model):
    
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=100,null=True,blank=False,)
    description = models.CharField(max_length=500,null=True,blank=False)
    image = models.ImageField(null=True,blank = False)
    created = models.DateTimeField(auto_now_add=True,auto_created=True)

    class Meta:
        ordering = ['-created']
        
    def __str__(self):
        return self.title