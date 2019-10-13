from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm
from .emails import send_welcome_email
from .models import User, Profile

def home(request):
    return render(request,'index.html')

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
def profile(request):
    profiles = Profile.objects.all()
    context = {
        "profiles":profiles
    }
    return render(request,'profile.html', context)
