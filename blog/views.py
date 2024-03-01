from django.shortcuts import render
from django.http.response import HttpResponse
from blog.models import Blog
# Create your views here.
def index(request):
    context = {'blog': Blog.objects.all()}
    return render(request,"blog/index.html", context)

def blogs(request):
    context = {'blog': Blog.objects.all()}
    return render(request,"blog/blog.html",context)

def blog_details(request ,id):
    return render(request,"blog/blog_details.html", {"id":id})
