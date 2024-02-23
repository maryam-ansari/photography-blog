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

def nav(request):
    user = User.objects.all()

    return render(request,'base/nav.html',{'user' : user})

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
    
def profile(request,id):
    user = User.objects.get(id=id)
    photo = Photo.objects.all().order_by('-created')
    print('user id : ',user.id)

    #account deletion
    if request.method == 'POST':
        user.delete()
        return redirect('home')

    context = {
        'user' : user,
        'photo' : photo
    }
    return render(request, 'base/profile.html',context)


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
            user=request.user,
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
def delete(request,id):
    photo = Photo.objects.get(id = id)
    
    
    if request.method == 'POST':
        #print('id : ',photo.id)
        photo.delete()
        return redirect('home')
    
    context = {'obj' : photo}

    return render(request, 'base/delete.html',context)


def read(request,id):
   
    photo = Photo.objects.get(id = id)
    msg = Comments.objects.all().order_by('-created')
    
    print('post : ', photo.title)
    
    if request.method == 'POST':
        add = Comments.objects.create(
            user=request.user,
            post=photo.title,
            message=request.POST.get('cmt')
            )
       
    context = {'objs' : photo,'msg' : msg}
    
    return render(request, 'base/read.html',context)

def delete_message(request,id):
    mem = Comments.objects.get(id=id)
    print('id :',mem)
    mem.delete()
    return redirect('home')



def about(request):
    return render(request,'base/about.html')