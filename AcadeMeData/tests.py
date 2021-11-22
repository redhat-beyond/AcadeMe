from django.test import TestCase
from AcadeMeData.models import Users


class TestUserModel(TestCase):

    def test_create_user(self):
        username = "username"
        password = "password"
        email = "user@example.com"
        type = "S"
        university = "RU"
        degree = "CS"
        user = Users.create_user(
            username, email, password, type, university, degree)
        assert isinstance(user, Users)
        assert user.user.username == username
        assert user.user.password == password
        assert user.user.email == email
        assert user.user.type == type
        assert user.user.university == university
        assert user.user.degree == degree

    def test_del_user(self):
        username = "username"
        password = "password"
        email = "user@example.com"
        type = "S"
        university = "RU"
        degree = "CS"
        user = Users.create_user(
            username, email, password, type, university, degree)
        assert isinstance(user, Users)
        assert Users.del_user(user)
