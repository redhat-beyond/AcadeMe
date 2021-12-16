from django.shortcuts import render
# redirect


def homePage(request):
    return render(request, 'landing/homepage.html')


def contact(request):
    return render(request, 'landing/contact_us.html')
