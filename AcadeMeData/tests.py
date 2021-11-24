import pytest
from AcadeMeData.models import User, Professor, University


class TestUserModel:
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
