import pytest
from AcadeMeData.models import User


@pytest.mark.django_db
class TestUserModel:
    def user_example(self):
        user_data = {'username': "username", 'password': "password", 'email': "user@example.com", 'type': "S",
                     'university': "RU",
                     'degree': "CS"}
        user = User.create_user(*user_data)
        return user

    def test_create_user(self):
        user_for_example = self.user_example()
        # users_list = User.objects.all()
        user = User.get_user('username')  # search for the user in the db by username
        assert user.get_username() == user_for_example.user.username
        assert user.email == user_for_example.user.email
        assert user.password == user_for_example.user.password
        # username. email, password are provided from django user. need to resolve how we get other fields

        # -----------all here is from previous - tests pass
        # assert users_list[len(users_list) - 1].user.username == user_data.user.username
        # assert users_list[len(users_list) - 1].user.email == user_data.user.email
        # assert users_list[len(users_list) - 1].user.password == user_data.user.password

        # assert users_list[len(users_list) - 1] == user_data  # is this enough? only check if the objects are equal

        # assert users_list[len(users_list) - 1].user.type == user_data.type  # this not working
        # assert users_list[len(users_list) - 1].user.university == user_data.university # this not working
        # assert users_list[len(users_list) - 1].user.degree == user_data.degree # this not working

    def test_del_user(self):
        user_for_example = self.user_example()
        # users_list = User.objects.all()
        assert User.del_user(user_for_example)
        user = User.get_user("username")
        assert user is None

    def test_get_user(self):
        user_for_example = self.user_example()
        # users_list = User.objects.all()
        # assert users_list[0].user.username == "user5"  # the first user in 0002_User_test_data
        assert User.get_user('username') == user_for_example.user
        # assert users_list[len(users_list) - 1] == user_for_example


@pytest.mark.django_db
class TestDegreeModel:
    def test_get_name(self):
        """
        Tests whether the degree name is correct.
        """

        test_degree = Degree(name='Computer Science').save()
        assert not test_degree.get_name() == 'Reichman University'

    def test_universities(self):
        """
        Tests whether a university offers this degree.
        """

        test_degree = Degree(name='Economics', universities='Reichman University').save()
        assert "Reichman University" in test_degree.universities()
        
