from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog

from django.views.generic import ListView, CreateView

# Create your views here.

class BlogCreateView(CreateView):
    model = Blog
    fields = '__all__'
    # queryset = Blog.objects.all()
    # queryset = Blog
    template_name_suffix = '_create'   
     
def home(request):
    blogs=Blog.objects.all
    return render(request,'blogapp/allblogs.htm',{'blogs':blogs})

def detail(request,id):
    blogs=Blog.objects.get(id=id)
    return render(request,'blogapp/detail.htm',{'blogs':blogs})
    
