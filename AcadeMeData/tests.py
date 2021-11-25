import pytest
from django.db.models import QuerySet
from AcadeMeData.models import User


class TestUserModel:
    def user_example(self):
        user_data = {'username': "username", 'password': "password", 'email': "user@example.com", 'type': "S",
                     'university': "RU",
                     'degree': "CS"}
        user = User.create_user(*user_data)
        return user  # , user_data

    @pytest.mark.django_db
    def test_create_user(self):
        users_list = User.objects.all()
        user_data = self.user_example()
        assert users_list[len(users_list) - 1].user.username == user_data.user.username
        assert users_list[len(users_list) - 1].user.email == user_data.user.email
        assert users_list[len(users_list) - 1].user.password == user_data.user.password

        assert users_list[len(users_list) - 1] == user_data  # is this enough?

        # assert users_list[len(users_list) - 1].user.type == user_data.type  # this now working
        # assert users_list[len(users_list) - 1].user.university == user_data.university # this now working
        # assert users_list[len(users_list) - 1].user.degree == user_data.degree # this now working

    @pytest.mark.django_db
    def test_del_user(self):
        users_list = User.objects.all()
        user_data = self.user_example()
        assert User.del_user(user_data)
        assert not users_list[len(users_list) - 1] == user_data

    @pytest.mark.django_db
    def test_get_user(self):
        users_list = User.objects.all()
        user_data = self.user_example()
        # assert users_list[0].user.username == "user5"
        assert users_list[len(users_list) - 1] == user_data

        # user = self.user_example()
        # user = User.get_user("username")
        # user.get_username()

    """"'@pytest
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
       
        # assert query_set.get_user("user1").email
        # query_set = User.objects.all() """

    """@pytest
    def test_del_user(self):
        user, user_data = self.user_example()
        assert isinstance(user, User)
        assert User.del_user(user)
        assert not (User.get_user(user_data.get('username')))


    @pytest
    def test_get_user(self):
        user, user_data = self.user_example()
        assert User.get_user(user_data.get('username')) == user """
