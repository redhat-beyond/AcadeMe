from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm, MessageForm
<<<<<<< HEAD
from .models import Messages, Course
from django.views.generic import ListView
=======
from .models import Messages
>>>>>>> bb74eaf (This is the alpha of the message board.)
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


<<<<<<< HEAD
class SearchResultsView(ListView):
    model = Course
    template_name = 'search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Course.objects.filter(name__icontains=query)

        return object_list


=======
>>>>>>> bb74eaf (This is the alpha of the message board.)
@login_required(login_url="/login/")
def msgboard(request):
    messages = Messages.objects.order_by('-msgDate')
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
    })
