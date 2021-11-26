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


class TestUniversityModel(pytest):
    @pytest
    def test_get_university_by_name(self):
        test_university = University(name='BS').save()
        universityTest = University.get_university_by_name(
            'BS')
        assert test_university == universityTest
        assert universityTest.exist()

    @pytest
    def test_get_university_by_location(self):
        test_university = University(location='Jerusalem').save()
        universityTest = University.get_university_by_location(
            'Jerusalem')
        assert test_university == universityTest
        assert universityTest.exist()


class TestProffesorModel:
    @pytest
    def test_get_name(self):
        test_proffesor = Professor(Proffesor='Dani the mani').save()
        assert test_proffesor.get_name() == "Dani the mani"

    @pytest
    def test_del_proffesor(self):
        test_proffesor = Professor(university='Dr arnold schwvartanager').save()
        assert isinstance(Professor, test_proffesor)
        assert Professor.del_Professor(test_proffesor)
        assert not Professor.del_Professor(test_proffesor)

    @pytest
    def test_create_professor(self):
        professor_data = {'professor_id': "professor_id",
                          'name': 'name',
                          'university': 'university',
                          'description': 'description',
                          'rate': 'rate'}
        professor = Professor.create_professor(*professor_data)
        assert isinstance(professor, Professor)
        assert professor.professor_id == professor_data.get('professor_id')
        assert professor.name == professor_data.get('name')
        assert professor.university == professor_data.get('university')
        assert professor.description == professor_data.get('description')
        assert professor.rate == professor_data.get('rate')
        assert professor.get_name() == professor_data.get('name')

