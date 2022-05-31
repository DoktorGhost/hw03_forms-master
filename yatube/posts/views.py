from django.shortcuts import render, get_object_or_404
from .models import Post, Group
import datetime as dt

def index(request):
    latest = Post.objects.all()[:10]
    return render(request, 'index.html', {'posts':latest})

def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:12]

    return render(request, 'group.html', {'group':group, 'posts':posts})

def year(request):
    year = dt.datetime.now().year
    return {'year':year}