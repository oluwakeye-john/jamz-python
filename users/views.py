from django.shortcuts import render, redirect
from .forms import UserCreateForm

from django.contrib.auth import login, authenticate

from django.contrib import messages

def register(request):
    if request.method == "POST":
        form = UserCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            login(request, user)
            messages.success(request, "Account created successfully")
            return redirect("home")
    else:
        form = UserCreateForm()

    return render(request, template_name="registration/register.html", context={
        "form":form
    })

def profile(request):
    return render(request, template_name="registration/profile.html")

# Create your views here.
