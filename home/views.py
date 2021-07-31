from django.shortcuts import render
from django.http import HttpResponse
from .models import User
# Create your views here.

# def creditPayHome(request):

#     # obj = User()
#     # obj.user_id = '778359'
#     # obj.user_name = 'Praveen Gopisetty'
#     # obj.user_email = 'Praveengopisetty1@gmail.com'
#     # obj.Occupation = 'Developer'

#     # obj = User.objects.all()

#     obj = User.objects.get(user_id = '778359')

#     # return render(request,"billing.html",{'user':obj} )
#     return render(request,"billing.html",{'user':obj} )

def creditPayHome(request):



    # return render(request,"billing.html",{'user':obj} )
    return render(request,"billing.html" )