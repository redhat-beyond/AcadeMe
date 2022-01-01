from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm, MessageForm
from .models import MessageBoards, Messages, Course
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required


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
    board = MessageBoards.objects.get(courseName = course_name)
    messages = Messages.objects.filter(board=board)
    form = MessageForm(initial={'userID': request.user.user})
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.userID = request.user.user
            instance.save()
            return redirect('msgboard')
    else:
        form = MessageForm()
    return render(request, '../templates/msgboard/board.html', {
        'messages': messages,
        'form': form,
        'course_name': course_name,
    })
