from django.shortcuts import render, redirect, get_object_or_404
from posts.models import Posts
from posts.form import PostForm

def index(request):
    posts = Posts.objects.all().order_by('-created_at')
    form = PostForm()
    return render(request, "index.html", {'posts': posts, "form":form})

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.save()
            return redirect('/')

def remove(request, post_id):
    post = get_object_or_404(Posts, id=post_id)
    
    if request.method == 'POST':
        post.delete()
        return redirect('/')

def update(request, post_id):
    post = get_object_or_404(Posts, id=post_id)
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
    
    return redirect("/")