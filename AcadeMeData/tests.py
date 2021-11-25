import pytest
from AcadeMeData.models import User


class TestUserModel:
    def user_example(self):
        data_for_user = {'username': "username", 'password': "password", 'email': "user@example.com", 'type': "S",
                         'university': "RU",
                         'degree': "CS"}
        user = User.create_user(*data_for_user)
        return user

    @pytest.mark.django_db
    def test_create_user(self):
        users_list = User.objects.all()
        user_data = self.user_example()
        assert users_list[len(users_list) - 1].user.username == user_data.user.username
        assert users_list[len(users_list) - 1].user.email == user_data.user.email
        assert users_list[len(users_list) - 1].user.password == user_data.user.password

        assert users_list[len(users_list) - 1] == user_data  # is this enough? only check if the objects are equal
        # if the line above enough then we can delete the first 3 assert line (username, email,password)

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
        # assert users_list[0].user.username == "user5"  # the first user in 0002_User_test_data
        assert users_list[len(users_list) - 1] == user_data
