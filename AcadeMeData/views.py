from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm, MessageForm
from .models import MessageBoards, Messages, Course
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from AcadeMe import views


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
    course_id = request.GET.get('course_id')
    print(course_id)
    course = Course.get_course_by_id(course_id)
    board = MessageBoards.get_msgboard_by_course(course)
    messages = Messages.objects.filter(board=board)
    form = MessageForm(initial={'userID': request.user.user})
    context = {'messages': messages,
               'form': form,
               'course_id': course_id,
               'course_name': course.name
               }
    views.add_navbar_links_to_context(request, context)
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.userID = request.user.user
            instance.board = board
            instance.save()
            return render(request, '../templates/msgboard/board.html', context)
    else:
        form = MessageForm()
    return render(request, '../templates/msgboard/board.html', context)
