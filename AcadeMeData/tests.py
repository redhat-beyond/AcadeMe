import pytest
from models import User


class TestUserModel(pytest):
    def user_example(self):
        user_data = {'username': "username", 'password': "password", 'email': "user@example.com", 'type': "S",
                     'university': "RU",
                     'degree': "CS"}
        user = User.create_user(*user_data)
        return user, user_data

    @pytest
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

    @pytest
    def test_del_user(self):
        user, user_data = self.user_example()
        assert isinstance(user, User)
        assert User.del_user(user)
        assert not (User.get_user(user_data.get('username')))

    @pytest
    def test_get_user(self):
        user, user_data = self.user_example()
        assert User.get_user(user_data.get('username')) == user
