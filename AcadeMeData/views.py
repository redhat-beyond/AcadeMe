from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm


def home(request):
    return render(request, 'users/home.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            message = "Your account has been created. You can log in now!"
            messages.success(request, f'{message}')
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'users/login.html', context)
