import pytest
from AcadeMeData.forms import UserRegistrationForm
from AcadeMeData.models import User


@pytest.fixture
def user_example():
    user_data = {'username': "shlomi", 'email': "user@example.com", 'password1': "daniboy246810",
                 'password2': "daniboy246810"}
    return user_data


@pytest.fixture
def user_bad_example():
    # username can't be none
    users_data = [
        {'username': "", 'email': "user@example.com", 'password1': "good password", 'password2': "good password"},
        # invalid email
        {'username': "good username", 'email': "user", 'password1': "good password", 'password2': "good password"},
        # passqords don't match
        {'username': "good username", 'email': "user@example.com", 'password1': "good password",
         'password2': "bad password"}]
    return users_data


@pytest.mark.django_db
class TestSignUp:
    def test_sign_up_invalid(self, user_bad_example):
        for user_data in user_bad_example:
            invalid = False
            form = UserRegistrationForm(data=user_data)
            try:
                form.save()
            except ValueError:
                invalid = True
            assert invalid

    def test_sign_up_valid(self, user_example):
        form = UserRegistrationForm(data=user_example)
        if form.is_valid():
            user = form.save()
            assert User.objects.filter(user=user.user).exists()
        else:
            assert False
