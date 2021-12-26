from django.shortcuts import render
from AcadeMeData.models import University, Degree


def app_layout(request):
    context = {}
    if request.user.is_authenticated:
        context['navbar_links'] = {f"Welcome {request.user.username}": "#", "Logout": "/logout"}
    else:
        context['navbar_links'] = {"Login": "/login", "Register": "/register"}
    return render(request, 'app_layout.html', context)


def homePage(request):
    all_universities = University.objects.all()
    all_degrees = Degree.objects.all()
    context = {'all_universities': all_universities, 'all_degrees': all_degrees}
    return render(request, 'landing/homepage.html', context)


def contact(request):
    return render(request, 'landing/contact_us.html')


def loginPage(request):
    return render(request, 'login/login.html')


def registrationPage(request):
    return render(request, 'registration/registration.html')


# def add_navbar_links_to_context(request):
#     context = {}
#     if request.user.is_authenticated:
#         context['navbar_links'] = {f"Welcome {request.user.username}": "#", "Logout": "/logout"}
#     else:
#         context['navbar_links'] = {"Login": "/login", "Register": "/register"}
#     return render(request, 'app_layout.html', context)
