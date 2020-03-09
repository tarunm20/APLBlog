from .models import Post

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def index(request):
    posts = Post.objects.all()
    form = AuthenticationForm()
    return render(request, 'app/index.html', {'posts':posts, 'form':form})

def post(request, id):
    post = Post.objects.get(id=id)

    return render(request, 'app/post.html', {'post':post})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app/index.html')
    else:
        form = UserCreationForm()

    return render(request, 'app/signup.html', {'form':form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('app/index.html')
    else:
        form = AuthenticationForm()

    return render(request, 'app/login.html', {'form':form})
