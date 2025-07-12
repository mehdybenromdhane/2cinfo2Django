from django.shortcuts import render,redirect

# Create your views here.

from django.contrib.auth import authenticate,login
def login_user(request):
    
    
    if request.method=="POST":
       name= request.POST['username']
       mdps = request.POST['password']
       
       
       user = authenticate(request , username=name , password=mdps)
       if user:
           login(request , user)
           return redirect('list')         
        
       else:
           return redirect('login_user') 
    
    
    
    return render (request,'person/login.html',{})