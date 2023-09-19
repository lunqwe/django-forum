from django.shortcuts import render, redirect
from .forms import RegisterForm, PostForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Post 


@login_required(login_url='/login')
def homepage(request):
    posts = Post.objects.all()
    sort_order = request.GET.get('sort', 'default')
    
    if request.method == "POST":
        post_id = request.POST.get("post-id")
        print(post_id)
    # sort_order = request.GET.get('sort', 'default')        
    # if sort_order == 'author':
    #     posts = posts.order_by('author').reverse()
    # elif sort_order == 'created_at':
    #     posts = posts.order_by('created_at').reverse()
    # elif sort_order == 'title':
    #     posts = posts.order_by('title') !!! 'sort_order': sort_order
    
    return render(request, 'main/home.html', {'posts' : posts})
    

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()
        
    return render(request, 'registration/sign_up.html', {"form" : form})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/home')
    else:
        form = PostForm()
    
    return render(request, 'main/create_post.html' , {"form" : form})

def delete_post(request):
    if request.method == "POST":
        post_id = request.POST.get('post_id')
        post = Post.objects.get(id=post_id)
        
        if post and request.user == post.author:
            post.delete()
            return redirect('homepage')
                