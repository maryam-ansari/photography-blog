from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render,redirect
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

#ADDED
from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Discussion, Comment
from .forms import DiscussionForm, CommentForm

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
       
    context = {'objs': photo,'msg': msg}
    
    return render(request, 'base/read.html',context)

def delete_message(request,id):
    mem = Comments.objects.get(id=id)
    print('id :',mem)
    mem.delete()
    return redirect('home')



def about(req):
    return render(req,'base/about.html')
    

# ADDED

def discussion_list(request):
    discussions = Discussion.objects.all()
    if discussions is None:
        discussions = []
    return render(request, 'base/discussion_list.html', {'discussions': discussions})

def discussion_detail(request, id):
    discussion = Discussion.objects.get(id=id)
    msg = Comment.objects.all().order_by('-created')

    if request.method == 'POST':
        add = Comment.objects.create(
            user=request.user,
            post=discussion.title,
            text=request.POST.get('cmt')
        )

    context = {'objs': discussion, 'msg': msg}
    return render(request, 'base/discussion_detail.html', context)


@login_required
def discussion_create(request):
    if request.method == 'POST':
        form = DiscussionForm(request.POST)
        if form.is_valid():
            discussion = form.save(commit=False)
            discussion.user_id = request.user.id
            discussion.description = request.POST.get('description')
            discussion.save()
            return redirect('discussion_list')
    else:
        form = DiscussionForm()

    return render(request, 'base/discussion_form.html', {'form': form})


@login_required(login_url='login')
def discussion_delete(request, id):
    discussion = Discussion.objects.get(id=id)

    if request.method == 'POST':
        # print('id : ',photo.id)
        discussion.delete()
        return redirect('discussion_list')

    context = {'obj': discussion}

    return render(request, 'base/delete.html', context)


def delete_discussion_message(request, discussion_id, id):
    msg = Comment.objects.get(id=id)
    print('id :',msg)
    msg.delete()

    return redirect('discussion_detail', id=discussion_id)

@login_required(login_url='login')
def discussion_update(request, t):
    discussion = Discussion.objects.get(title=t)

    form = DiscussionForm(instance=discussion)

    if request.method == 'POST':
        form = DiscussionForm(request.POST, instance=discussion)
        if form.is_valid():
            form.save()
            return redirect('discussion_list')

    context = {'form': form, 'title': discussion}
    return render(request, 'base/discussion_update.html', context)
