from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from django.views.generic import ListView
from .models import Course


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


class SearchResultsView(ListView):
    model = Course
    template_name = 'search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Course.objects.filter(name__icontains=query)

        return object_list
