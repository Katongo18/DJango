from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
#from django.http import HttpResponse
import time

from .models import Post


# Create your views here.


'''posts = [

    {

        'author':'Jane doe',
        'title': 'Blog post 1',
        'content':'First blog post',
        'date': str(time.ctime())
    },
     {

        'author':'Corey MS',
        'title': 'Blog post 2',
        'content':'Second blog post',
        'date': str(time.ctime())
    }


]'''

def home(request):
    # content = {'posts':posts}
    content = {'posts':Post.objects.all()}
    # return HttpResponse('<h1> Blog Home!</h1>')
    return render(request, 'blog/home.html', content)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    
 

def about(request):
   #return HttpResponse('<h1> About Blog </h1>')
    return render(request, 'blog/about.html', {'title':'About'})
