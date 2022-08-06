from django.shortcuts import render
from mainapp.models import *
# Create your views here.
def base(request):
    news=MainPageBD.objects.all()
    return render(request,"base.html",{"news":news})