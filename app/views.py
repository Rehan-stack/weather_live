from django.shortcuts import render

# Create your views here.


def index(request):
    cities = ['london','karachi']
    return render(request,'index.html',{'cities':cities})