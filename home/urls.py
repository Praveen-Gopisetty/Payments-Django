from django.urls import path
from .import views

urlpatterns = [
    
    path('billing',views.creditPayHome ,name='creditPayHome')

]