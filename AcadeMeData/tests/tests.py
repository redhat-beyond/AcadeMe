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
    def generate_university(self, university_id=1, name='Reichman University', location="Herzlia",
                            description="A nice place"):
        university = University(university_id=university_id, name=name, location=location,
                                description=description)
        university.save()
        return university

    def test_get_university_by_name(self, university_id=1, name='Reichman University', location="Herzlia",
                                    description="A nice place"):
        test_university = self.generate_university(university_id, name, location, description)
        university_test = University.get_university_by_name(name)
        assert test_university == university_test
        assert isinstance(university_test, University)

    def test_get_university_by_location(self, university_id=1, name='Reichman University', location="Herzlia",
                                        description="A nice place"):
        test_university = self.generate_university(university_id, name, location, description)
        university_test = University.get_university_by_location(location)
        assert test_university == university_test
        assert isinstance(university_test, University)


@pytest.mark.django_db
class TestProfessorModel:
    def generate_professor(self, professor_id=1, name="DR Arnold Schwarzenegger", university=None,
                           description="A cool guy who looked familliar", rate=4.5, university_id=1,
                           uni_name='Reichman University', location="Herzlia",
                           uni_description="A nice place"):
        university = TestUniversityModel.generate_university(self, university_id, uni_name, location, uni_description)
        professor = Professor.create_professor(professor_id=professor_id,
                                               name=name,
                                               university=university,
                                               description=description,
                                               rate=rate)
        return professor

    def test_get_name(self, professor_id=1, name="DR Arnold Schwarzenegger", university=None,
                      description="A cool guy who looked familliar", rate=4.5, university_id=1,
                      uni_name='Reichman University', location="Herzlia",
                      uni_description="A nice place"):
        university = TestUniversityModel.generate_university(self, university_id, uni_name, location, uni_description)
        professor_for_example = self.generate_professor(professor_id, name, university, description, rate)
        assert professor_for_example.get_name() == name

    def test_create_professor(self, professor_id=1, name="DR Arnold Schwarzenegger", university=None,
                              description="A cool guy who looked familliar", rate=4.5, university_id=1,
                              uni_name='Reichman University', location="Herzlia",
                              uni_description="A nice place"):
        university = TestUniversityModel.generate_university(self, university_id, uni_name, location, uni_description)
        professor_for_example = self.generate_professor(professor_id, name, university, description, rate)
        professor = Professor.get_professor(name)
        assert professor.get_name() == professor_for_example.name
        assert professor.get_description() == professor_for_example.description
