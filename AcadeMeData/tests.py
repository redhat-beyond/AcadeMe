import pytest
from django.db.models import QuerySet
from django.contrib.auth.models import User
from academedata.models import User
from academedata.models import Degree


@pytest.mark.django_db
def user_example(self):
    user_data = {'username': "username", 'password': "password", 'email': "user@example.com", 'type': "S",
                'university': "RU", 'degree': "CS"}
    user = User.create_user(*user_data)
    return user, user_data


@pytest.mark.django_db
def test_create_user(self):
    user, user_data = self.user_example()
    assert isinstance(user, User)
    assert user.username == user_data.get('username')
    assert user.password == user_data.get('password')
    assert user.email == user_data.get('email')
    assert user.type == user_data.get('type')
    assert user.university == user_data.get('university')
    assert user.degree == user_data.get('degree')
    assert User.get_user(user_data.get('username')).degree == user_data.get('degree')


@pytest.mark.django_db
def test_del_user(self):
    user, user_data = self.user_example()
    assert isinstance(user, User)
    assert User.del_user(user)
    assert not (User.get_user(user_data.get('username')))


@pytest.mark.django_db
def test_get_user(self):
    user, user_data = self.user_example()
    assert User.get_user(user_data.get('username')) == user

@pytest.mark.django_db
def test_get_user(self):
    user, user_data = self.user_example()
    assert User.get_user(user_data.get('username')) == user


@pytest.mark.django_db
def test_get_name(self):
    """
    Tests whether the degree name is correct.
    """

test_degree = Degree(degree='Computer Science').save()
assert not test_degree.get_name() == 'Reichman University'


@pytest.mark.django_db
def test_universities(self):
    """
    Tests whether a university offers this degree.
    """

test_degree = Degree(degree='Economics', universities='Reichman University').save()
assert "Reichman University" in test_degree.universities()
