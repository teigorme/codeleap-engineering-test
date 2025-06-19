from django.shortcuts import render, redirect, get_object_or_404
from posts.models import Posts
from posts.form import PostForm
from django.contrib.sessions.backends.db import SessionStore


def login(request):
    if request.session.get('username'):
        return redirect('/')
    

    if request.method == "POST":
        username = request.POST.get('username', '').strip()
        if username:  
            request.session['username'] = username
            return redirect('/')
    return render(request, "login.html")    


def logout(request):
    if 'username' in request.session:
        del request.session['username']
    return redirect('/login')


def index(request):
    username = request.session.get('username')
    if not username:
        return redirect('/login')
    
    posts = Posts.objects.all().order_by('-created_at')
    form = PostForm()
    return render(request, "index.html", {'posts': posts, "form":form})

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.username = request.session.get('username')
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