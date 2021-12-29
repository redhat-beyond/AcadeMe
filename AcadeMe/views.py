from django.shortcuts import render
from AcadeMeData.models import Course, Degree, University


def app_layout(request):
    return render(request, 'app_layout.html')


def homePage(request):
    all_universities = University.objects.all()
    all_degrees = Degree.objects.all()
    context = {'all_universities': all_universities, 'all_degrees': all_degrees}
    add_navbar_links_to_context(request, context)
    return render(request, 'landing/homepage.html', context)


def courseList(request):
    context = {}
    seluniversity = request.POST.get('selectUniversity', None)
    seldegree = request.POST.get('selectDegree', None)
    context['seluniversity'] = seluniversity
    context['seldegree'] = seldegree
    all_courses = Course.objects.all()
    context['all_courses'] = all_courses
    add_navbar_links_to_context(request, context)
    return render(request, 'landing/course-list-page.html', context)


def course(request):
    context = {}
    goToCourse = request.POST.get('goTo', None)
    context['goToCourse'] = goToCourse
    all_courses = Course.objects.all()
    for course in all_courses:
        if course.name == goToCourse:
            selectedCourse = Course.objects.get(name=goToCourse)
    context['selectedCourse'] = selectedCourse
    add_navbar_links_to_context(request, context)
    return render(request, 'landing/course-page.html', context)


def contact(request):
    context = {}
    add_navbar_links_to_context(request, context)
    return render(request, 'landing/contact-us.html', context)


def loginPage(request):
    return render(request, 'login/login.html')


def registrationPage(request):
    return render(request, 'registration/registration.html')


def add_navbar_links_to_context(request, context):
    if request.user.is_authenticated:
        context['navbar_links'] = {f"Welcome {request.user.username}": "#", "Logout": "/logout"}
    else:
        context['navbar_links'] = {"Login": "/login", "Register": "/register"}
