from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm, MessageForm
from .models import MessageBoards, Messages, Course
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from AcadeMe import views
from django.urls import reverse




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



@login_required(login_url="/login/")
def msgboard(request):
    course_name = request.GET.get('course_name')
    course = Course.get_course_by_name(course_name)
    board = MessageBoards.get_msgboard_by_course(course)
    messages = Messages.objects.filter(board=board)
    form = MessageForm(initial={'userID': request.user.user})
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.userID = request.user.user
            instance.board = board
            instance.save()
            return redirect('msgboard', {'course_name': course_name})
    else:
        form = MessageForm()
    context = {'messages': messages,
               'form': form,
               'course_name': course_name,
               'course' : course
               }
    views.add_navbar_links_to_context(request, context)
    return render(request, '../templates/msgboard/board.html', context)

