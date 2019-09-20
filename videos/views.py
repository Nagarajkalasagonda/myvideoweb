from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime
from django.contrib import messages


@login_required(login_url='login')
def list_video(request):
    if request.method=='GET':
        user=UserReg.objects.get(user=request.user)
        videos = Videos.objects.filter(owner=user)
        
        return render(request,"list_video.html",{'user':user,'videos':videos})

    elif request.method=='POST':
        search = request.POST['search']
        user=UserReg.objects.get(user=request.user)
        videos = Videos.objects.filter(owner=user,title__icontains=search)
        return render(request,"list_video.html",{'user':user,'videos':videos})


@login_required(login_url='login')
def update_video(request,pk):
    if request.method=='GET':
        #print ("kkkkkkkkkkkkkkkkk"+pk)
        user=UserReg.objects.get(user=request.user)
        videos = Videos.objects.get(pk=pk)
        return render(request,"update_video.html",{'user':user,'videos':videos})
    elif request.method=='POST':
        #print('qqqqqqqqq')
        #print("qqqqqqqqqqqqqqqqqqqqqqqqq"+str(request.POST)+'           '+str(request.FILES))
        videos = Videos.objects.get(pk=pk)
        title = request.POST['title']
        description = request.POST['description']
        tag = request.POST['tag']
        referenceid=request.POST['referenceid']
        category = request.POST['category']
        
        vid_db = Videos.objects.get(pk=pk)
        vid_db.title = title
        vid_db.description = description
        vid_db.referenceid = referenceid
        vid_db.tag = tag
        vid_db.category = category
        vid_db.save()
        
        print(title,description,tag,category)
        lastdate = datetime.datetime.now()
        
        messages.info(request,'Video updated succesfully')

        return redirect('/list_video')

@login_required(login_url='login')
def create_video(request):
    if request.method=='GET':
        user = UserReg.objects.get(user=request.user)
       
        return render(request,"create_video.html",{'user':user})
    elif request.method=='POST':
        #print('qqqqqqqqq')
        print("qqqqqqqqqqqqqqqqqqqqqqqqq"+str(request.POST)+'           '+str(request.FILES))
        title = request.POST['title']
        description = request.POST['description']
        tag = request.POST['tag']
        referenceid=request.POST['referenceid']
        category = request.POST['category']
        video_file =  request.FILES['video_upload'] 
        
        print(title,description,tag,category)
        date = datetime.datetime.now()
        video_db = Videos.objects.create(title=title,
                    description=description,
                    tag=tag,
                    owner=UserReg.objects.get(user=request.user),
                    category=category,
                    referenceid=referenceid,
                    lastdate=date,
                    video=video_file
                    )
        messages.info(request,'Video created succesfully')
        return redirect('/list_video')


def login(request):
    if request.method=='POST':
        username = request.POST['email']
        password = request.POST['pass']
        #print(username,password)
        user = auth.authenticate(username=username,password=password)
        #for user session 
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Username or password not matching')
            return redirect('/login')
    else:
        return render(request,"user_loginpage.html")
    

def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email =request.POST['email']
        contact=request.POST['contact']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
       
        if password1==password2:
            if User.objects.filter(username=username).exists():
              
                messages.info(request,'Username Taken')
                return redirect('register')
           
            else:
                user= User.objects.create_user(username=username,password=password1,first_name=first_name,last_name=last_name)
                user.save()
                user_reg = UserReg.objects.create(user=user,
                    name=first_name +' '+last_name,
                    email=email,
                    contact=contact)
                print("User Created")
                return redirect('login')
                
        else:
            messages.info(request,'Password not matching')
            return redirect('/')
    else:
        return render(request,'register.html')


@login_required(login_url='login')
def index(request):

    if request.method=='GET':
        print('Test user'+request.user.username)

        user = UserReg.objects.get(user=request.user)
        return render(request,"index.html",{'user':user})

