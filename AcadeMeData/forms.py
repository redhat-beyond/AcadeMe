from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from AcadeMeData.models import User, DjangoUser, Degree, University, UNIVERSITYCHOICES, DEGREECHOICES


class UserRegistrationForm(UserCreationForm):
    university = forms.ModelChoiceField(University.objects, required=False)
    degree = forms.ModelChoiceField(Degree.objects, required=False)
    email = forms.EmailField(required=True)

    class Meta1:
        model = DjangoUser
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        user2 = User(user=user, university=self.cleaned_data['university'], degree=self.cleaned_data['degree'])
        user2.save()
        return user2
