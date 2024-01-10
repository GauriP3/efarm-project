from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')

def SignupPage(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        mname=request.POST.get('mname')
        lname=request.POST.get('lname')
        age=request.POST.get('age')
        mob_no=request.POST.get('mob_no')
        dob=request.POST.get('dob')
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confiorm password are not Same!!")
        else:
            my_user=User.objects.create_user(username=uname, email=email, password=pass1,
                                              first_name=fname, last_name=lname)
            my_user.age = age
            my_user.mob_no = mob_no
            my_user.dob = dob
            my_user.save()
            return redirect('login')
        



    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')