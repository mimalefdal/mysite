from django.shortcuts import render,get_object_or_404
from blog.models import *

# Create your views here.
def blog_dev(request):
        posts = Post.objects.all()
        content = {'posts':posts}
        return render(request,'blog/dev.html',content)

def blog_view(request):
        return render(request,'blog/blog-home.html')


def blog_single_view(request,id):
        post = get_object_or_404(Post,id=id,published=True)
        content={'post':post}
        return render(request,'blog/blog-single.html',content)
    