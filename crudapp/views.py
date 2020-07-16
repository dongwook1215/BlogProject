from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone


# Create your views here.

def main(request):
    blog=Blog.objects.all().order_by('-id')
    return render(request,'main.html',{'blog':blog})

def detail(request,object_id):
    blog_detail=get_object_or_404(Blog,pk=object_id)
    return render(request,'detail.html',{'blog_detail':blog_detail})

def create(request):
    return render(request,'create.html')

def pop(request):
    blog=Blog()
    blog.title=request.GET['title']
    blog.body=request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/')

def recreate(request, object_id):
    blog=get_object_or_404(Blog,pk=object_id)
    return render(request,'recreate.html',{'blog_detail':blog})

def update(request, object_id):
    blog=get_object_or_404(Blog,pk=object_id)
    blog.title=request.GET['title']
    blog.body=request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/detail/'+str(blog.id))

def remove(request, object_id):
    blog=get_object_or_404(Blog,pk=object_id)
    blog.delete()
    return redirect('/')
    