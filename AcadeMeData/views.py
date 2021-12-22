from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from AcadeMeData.models import University, Degree


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
    return render(request, '../templates/registration/registration.html', context)


def universities_degrees(request):
    all_universities = University.objects.all()
    all_degrees = Degree.objects.all()
    #     University.get_universities() # added this function in models.py
    context = {'all_universities': all_universities, 'all_degrees': all_degrees}
    return render(request, '../templates/landing/homepage.html', context)

# def degrees(request):
#     all_degrees = Degree.objects.all()
#
#     context = {'all_degrees': all_degrees}
#     return render(request, '../templates/landing/homepage.html', context)
