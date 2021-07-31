from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth, User
from django.contrib import messages

# Create your views here.

def login(request):


    if request.method == 'POST':
        name = request.POST['your_name']
        passwd = request.POST['your_pass']

        user = auth.authenticate(username=name,password = passwd)

        if user is not None:
            auth.login(request,user)
            # obj = User.objects.get(user_id = '778359')
            
            return redirect("home/billing", user = user)
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('')
    else:
        return render(request,'login.html')

def logout(request):

    auth.logout(request)
    return redirect('/')

        






    