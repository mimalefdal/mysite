from django.shortcuts import render
from blog.models import *

# Create your views here.
def blog_index(request):
        posts = Post.objects.all()
        content = {'posts':posts}
        return render(request,'blog/index.html',content)

def blog_view(request):
        return render(request,'blog/blog-home.html')


def blog_single_view(request):
        return render(request,'blog/blog-single.html')
    