from django.shortcuts import render
from .forms import signup
from django.contrib.auth.forms import AuthenticationForm
from django.contrib .auth import authenticate,login,logout
from django.shortcuts import render,HttpResponseRedirect
from django.contrib import messages

# Create your views here.
def Login(request):
    if not request.user.is_authenticated:
            if request.method =="POST":
                form=AuthenticationForm(request.POST,data=request.POST)
                if form.is_valid():
                    uname=form.cleaned_data['username'] 
                    upass=form.cleaned_data['password']
                    user = authenticate(username=uname,password=upass)
                    if user is not None:
                        login(request,user)
                        messages.success(request,'logged in successfully !!')
                        return HttpResponseRedirect("/dashboard/")
            else:
                form=AuthenticationForm()
            return render(request,'login.html',{'form':form})
    else:
        return HttpResponseRedirect("/")
    

# SIGNUP PAGE
def SignupPage(request):
    if request.method == 'POST':
        fm = signup(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Account Created Succefully')
            return HttpResponseRedirect('/')
    else:
        fm = signup()
    return render(request,'signup.html',{'form':fm})


def Dashboard(request):
    return render(request, 'dashboard.html')


# LOGOUT PAGE
def userlogout(request):
    logout(request)
    return HttpResponseRedirect('/')