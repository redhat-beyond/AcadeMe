from django.shortcuts import render


def app_layout(request):
    return render(request, 'app_layout.html')


def homePage(request):
    return render(request, 'landing/homepage.html')


def contact(request):
    return render(request, 'landing/contact_us.html')


def loginPage(request):
    return render(request, 'login/login.html')


def registrationPage(request):
    return render(request, 'registration/registration.html')
