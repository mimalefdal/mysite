from django.shortcuts import render,get_object_or_404
from blog.models import *
from django.utils import timezone

# Create your views here.
def blog_view(request):
        posts = Post.objects.filter(date_published__lte=timezone.now())
        content = {'posts':posts}
        return render(request,'blog/blog-home.html',content)


def blog_single_view(request,id):
        post = get_object_or_404(Post,id=id,published=True)

        post.counted_view += 1
        post.save()
        
        content={'post':post}
        return render(request,'blog/blog-single.html',content)
