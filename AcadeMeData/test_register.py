import pytest
from AcadeMeData.forms import UserRegistrationForm
from AcadeMeData.models import User


@pytest.fixture
def user_example():
    user_data = {'username': "daniel", 'email': "user@example.com", 'password1': "D4587450", 'password2': "D4587450",
                 'university': "Hebrew University", 'degree': "Computer Science"}
    return user_data


@pytest.fixture
def user_bad_example():
    # username can't be none
    users_data = [
        {'username': "", 'email': "user@example.com", 'password1': "good password", 'password2': "good password",
         'university': "RU", 'degree': "CS"},
        # invalid email
        {'username': "good username", 'email': "user", 'password1': "good password", 'password2': "good password",
         'university': "RU", 'degree': "CS"},
        # passqords don't match
        {'username': "good username", 'email': "user@example.com", 'password1': "good password",
         'password2': "bad password", 'university': "RU", 'degree': "CS"}]
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
            assert User.user.objects.filter(pk=user.user.username).exists()
        else:
            assert False
