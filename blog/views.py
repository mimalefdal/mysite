from django.shortcuts import render
from blog.models import *

# Create your views here.
def blog_dev(request):
        posts = Post.objects.all()
        content = {'posts':posts}
        return render(request,'blog/dev.html',content)

def blog_view(request):
        return render(request,'blog/blog-home.html')


def blog_single_view(request,id='0'):
        content={'id':id}
        return render(request,'blog/blog-single.html',content)
    