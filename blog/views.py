from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
      'author': 'Minh',
      'title': 'Blog post 1',
      'content': 'First post content',
      'date_posted': 'August 27, 2023' 
    },
    {
      'author': 'My',
      'title': 'Blog post 2',
      'content': 'Second post content',
      'date_posted': 'August 28, 2023' 
    }
]

def home(request):
    context= {
        'posts': posts
    }
    print(request)
    return render(request, 'blog/home.html', {'title':'Home', 'posts':posts})

def about(request):
    return render(request, 'blog/about.html',{'title':'About', 'posts':posts})
