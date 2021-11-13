from django.shortcuts import render
#redirect
def landingPage(request):
    return render(request, 'landingpage/landing_page.html')

