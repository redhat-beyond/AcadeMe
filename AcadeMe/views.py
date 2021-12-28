from django.shortcuts import render
import pdb

from AcadeMeData.models import Course, Degree, University


def app_layout(request):
    return render(request, 'app_layout.html')


def homePage(request):
    universities = University.objects.all()
    degrees = Degree.objects.all()
    return render(request, 'landing/homepage.html', {
        "universities": universities,
        "degrees": degrees,
    })


def courseList(request):
    context = {}
    seluniversity = request.POST.get('selectUniversity', None)
    seldegree = request.POST.get('selectDegree', None)
    context['seluniversity'] = seluniversity
    context['seldegree'] = seldegree
    all_courses = Course.objects.all()
    context['all_courses'] = all_courses
    # for degree in Degree.objects.all():
    #     if degree.name == 'Computer Science':
    #         course_degree = degree.name
    # context['course_degree'] = course_degree
    return render(request, 'landing/course-list-page.html', context)


def contact(request):
    return render(request, 'landing/contact-us.html')


def loginPage(request):
    return render(request, 'login/login.html')


def registrationPage(request):
    return render(request, 'registration/registration.html')
