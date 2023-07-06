from django.shortcuts import render
from django.http import HttpResponse
from .models import Post,Category
# Create your views here.
def home(request):
    posts=Post.objects.all()[0:10]

    cats=Category.objects.all()

    data={
        'posts': posts,
        'cats': cats,
    }
    
    return render(request, 'home.html',data)

def post(request,url):  
    post=Post.objects.get(url=url)
    cats=Category.objects.all()
    data={
        'post': post,
        'cats': cats,
    }
    return render(request, 'posts.html',data)

def category(request,url):
    cat=Category.objects.get(url=url)
    post=Post.objects.filter(cat=cat)
    data={
        'post': post,
        'cat': cat,
    } 
    return render(request,'category.html',data)