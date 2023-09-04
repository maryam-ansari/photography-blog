from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render,redirect
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.



def home(request):
    search = request.GET.get('search') if request.GET.get('search') != None else ''
    categories = Category.objects.filter(name__contains=search)
    data = request.GET.get('category')
   
    if data != None:
        photo = Photo.objects.filter(category__name=data)
    else:
        photo = Photo.objects.all()
    
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        print('user',username)
        print('pwd',password)
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,"User doesnot exists")

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request,"User name or password is invalid")
    #users = User.objects.all
    context = {'categories' : categories,'photo' : photo}
    return render(request, 'base/home.html',context)
    
   


def logoutUser(request):

    logout(request)
    return redirect('home')

def loginUser(request):

    return render(request,'base/login.html')

def registerUser(request):
    page = 'register'
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
        else:
            messages.error(request," An unexpected error occured !")
    return render(request,'base/register.html',{'form' : form})

@login_required(login_url='login')
def upload(request):
    categories = Category.objects.all()
    photo = Photo.objects.all()


    if request.method == 'POST':
        data = request.POST
        img = request.FILES.get('image')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != 'none':
            category, created = Category.objects.get_or_create(
                name=data['category_new']
            )
        else:
            category = None

        photo = Photo.objects.create(
            category = category,
            title = data['title'],
            description = data['description'],
            image = img,
        )

        return redirect('home')
    

    context = {'categories' : categories,'photo' : photo}
    return render(request, 'base/upload.html',context)
    
@login_required(login_url='login')
def update(request,t):
    photo = Photo.objects.get(title = t)
    
    form = PhotoForm(instance = photo)

    if request.method == 'POST':
        form = PhotoForm(request.POST, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    
    context = {'form': form,'title':photo}
    return render(request,'base/update.html',context)

@login_required(login_url='login')
def delete(request,t):
    #categories = Category.objects.get(id=fk)
    photo = Photo.objects.get(title = t)
    
    if request.user == photo.user:    
        if request.method == 'POST':
            photo.delete()
            #photo.category.delete()
            return redirect('home')
    
    context = {'obj' : photo}

    return render(request, 'base/delete.html',context)


def read(request,t):
    #categories = Category.objects.get(id=fk)
    photo = Photo.objects.get(title = t)
    msg = Comments.objects.all().order_by('-created')

    if request.method == 'POST':
        add = Comments.objects.create(
            user=request.user,
            message=request.POST.get('cmt')
        )
        #print('cmts : ',request.POST.get('cmt'))
        #return redirect('read',photo.title)

       
       

    context = {'objs' : photo,'msg' : msg}

    return render(request, 'base/read.html',context)

def delete_message(request,id):
    mem = Comments.objects.get(id=id)
    print('id :',mem)
    mem.delete()
    
    return redirect('home')
