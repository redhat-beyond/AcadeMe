from django.test import TestCase
from AcadeMeData.models import User


class TestUserModel(TestCase):

    def test_create_user(self):
        username = "username"
        password = "password"
        email = "user@example.com"
        type = "S"
        university = "RU"
        degree = "CS"
        user = User.create_user(
            username, email, password, type, university, degree)
        assert isinstance(user, User)
        assert user.username == username
        assert user.password == password
        assert user.email == email
        assert user.type == type
        assert user.university == university
        assert user.degree == degree

    def test_del_user(self):
        username = "username"
        password = "password"
        email = "user@example.com"
        type = "S"
        university = "RU"
        degree = "CS"
        user = User.create_user(
            username, email, password, type, university, degree)
        assert isinstance(user, User)
        assert User.del_user(user)
