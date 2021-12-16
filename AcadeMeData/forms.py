from django import forms
from django.contrib.auth.forms import UserCreationForm
from AcadeMeData.models import User, DjangoUser, UNIVERSITYCHOICES, DEGREECHOICES


class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'id': 'selectContent', 'placeholder': 'Enter Passowrd'})
    )
    password2 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'id': 'selectContent', 'placeholder': 'Enter Passowrd'})
    )

    university = forms.ChoiceField(choices=UNIVERSITYCHOICES.choices, required=False,
                                   widget=forms.Select(attrs={'id': 'selectContent'}))
    degree = forms.ChoiceField(choices=DEGREECHOICES.choices, required=False,
                               widget=forms.Select(attrs={'id': 'selectContent'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'id': 'selectContent', 'placeholder': 'Enter e-mail'}))

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
