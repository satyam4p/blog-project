from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from basicapp.forms import userform,profileform
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    return render(request,'basicapp/index.html')


def special(request):
    return render(request,'basioapp/index.html')


@login_required()
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):

    registered=False

    if request.method =="POST":
        #get info from both forms
        user_form=userform(data=request.POST)
        profile_form=profileform(data=request.POST)

        #check if both forms are valid
        if user_form.is_valid() and profile_form.is_valid():
            #save user_form to database
            user=user_form.save()

            #hash the password

            user.set_password(user.password)

            user.save()

            #update the profile and profolio site

            profile=profile_form.save(commit=False)

            #set ie to one relationship btw user

            profile.user=user
            #check if profile pic is provided

            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']
            #now save the form
            profile.save()
            registered=True

        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form=userform()
        profile_form=profileform()
    return render(request,'basicapp/register.html',{'user_form':user_form,
                                                    'profile_form':profile_form,
                                                    'registered':registered,})


def user_login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse("index"))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")

        else:
            print("someone tried to login and failed")
            print("USERNAME:{} and password:{}".format(username,password))
            return HttpResponse("invalid account info")

    else:
        return render(request,'basicapp/login.html',{})











