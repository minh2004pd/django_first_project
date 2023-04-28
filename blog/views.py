from django.shortcuts import render
from blog.models import Post
from django.http import HttpResponse

def home(request):
    context= {
        'posts': Post.objects.all()
    }
    print(request)
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html',{'title':'About', 'posts':posts})
