from django.shortcuts import render
from . models import MyBlog

# Create your views here.
def index(request):
    mypost = MyBlog.objects.all()
    return render(request, 'index.html',{'mypost':mypost})

def getpost(request,pk):
    mypost = MyBlog.objects.get(id=pk)
    return render(request, 'mypost.html',{'mypost':mypost})