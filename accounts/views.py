from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.

def signup(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        pswd = request.POST['pswd']
        re_pass = request.POST['re_pass']
        if pswd == re_pass:
            if User.objects.filter(username=name).exists():
                messages.info(request,'User Name Taken')
                return redirect('signup')

            elif User.objects.filter(email = email).exists():
                messages.info(request,'Email Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=name,email=email,password=pswd)
                user.save()
                return redirect('/')
        else:
            messages.info(request,'Password not matching')
            return redirect('signup')
    else:
        return render(request,'signup.html')
    return render(request,"signup.html" )