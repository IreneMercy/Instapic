from django.shortcuts import render, redirect, HttpResponse, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
from .emails import send_welcome_email
from .models import User, Profile, Post, Comment


def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password1=form.cleaned_data['password1']
            recipient=User(username=username,email=email)
            send_welcome_email(username,email)
            messages.success(request, f'Account has been created successfully!')
            return redirect('login')
    else:
        form = RegisterForm()
    context = {
        'form':form,
    }
    return render(request, 'users/register.html', context)


@login_required
def post(request):
    posts = Post.objects.all()
    comments = Comment.objects.all()
    comment_form = CommentForm()
    context = {
        "posts":posts,
        "comment_form":comment_form,
        "comments":comments
    }
    return render(request,'posts.html', context)



@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
    else:
        form = PostForm()
    context = {
        "form":form,
    }
    return render(request, 'post_create.html', context)

@login_required
def comment(request, post_id):
    comment_form = CommentForm()
    post = Post.objects.filter(pk=post_id).first()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('posts')
    else:
        comment_form = CommentForm()
    context = {
        "comment_form":comment_form,
    }
    return render(request, 'posts.html', context)

@login_required
def profile(request):
    posts = Post.objects.all()
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been successfully updated')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
    'user_form':user_form,
    'profile_form':profile_form,
    'posts':posts,
    }
    return render(request, 'profile.html', context)
