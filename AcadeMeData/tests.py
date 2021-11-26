import pytest
from AcadeMeData.models import User, Professor, University


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


@pytest.mark.django_db
class TestUniversityModel:
    def university_example(self):
        university = University(university_id=1, name='Reichman University', location="Herzlia",
                                description="A nice place")
        university.save()
        return university

    def test_get_university_by_name(self):
        test_university = self.university_example()
        university_test = University.get_university_by_name(
            'Reichman University')
        assert test_university == university_test
        assert isinstance(university_test, University)

    def test_get_university_by_location(self):
        test_university = self.university_example()
        university_test = University.get_university_by_location(
            'Herzlia')
        assert test_university == university_test
        assert isinstance(university_test, University)


@pytest.mark.django_db
class TestProffesorModel:
    def proffesor_example(self):
        university = TestUniversityModel.university_example(self)
        professor = Professor.create_professor(professor_id=1,
                                               name="DR Arnold Schwarteneiger",
                                               university=university,
                                               description="A cool guy who lookd familliar",
                                               rate=4.5)
        return professor

    def test_get_name(self):
        professor_for_example = self.proffesor_example()
        assert professor_for_example.get_name() == "DR Arnold Schwarteneiger"

    def test_create_professor(self):
        professor_for_example = self.proffesor_example()
        professor = Professor.get_proffesor('DR Arnold Schwarteneiger')
        assert professor.get_name() == professor_for_example.name
        assert professor.get_description() == professor_for_example.description
