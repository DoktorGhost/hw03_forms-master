from django.shortcuts import redirect, render, get_object_or_404
from .forms import PostForm
from .models import Post, Group
import datetime as dt
from django.contrib.auth.decorators import login_required



def index(request):
    latest = Post.objects.all()[:10]
    return render(request, 'index.html', {'posts':latest})

def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:12]
    return render(request, 'group.html', {'group':group, 'posts':posts})

@login_required
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("index")
    form = PostForm()
    return render(request, 'new.html', {'form':form})

def year(request):
    year = dt.datetime.now().year
    return {'year':year}