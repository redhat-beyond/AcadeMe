import pytest
from AcadeMeData.models import University, Degree, Professor, User, Course


@pytest.fixture
def generate_university(university_id=5, name='The Technion', location="Haifa",
                        description="Best University in Israel"):
    university = University(university_id=university_id, name=name, location=location,
                            description=description)
    university.save()
    return university


@pytest.fixture
def generate_degree(degree_id=1, name='History101', universities="Ben Gurion University, Reichman University",
                    description="Learn about historic events and their influences on the world"):
    degree = Degree.create_degree(degree_id=degree_id, name=name, universities=universities,
                                  description=description)
    degree.save()
    return degree


@pytest.fixture
def generate_professor(generate_university, professor_id=2, name="DR Arnold Schwarzenegger",
                       description="A cool guy who looked familiar", rate=4.5):
    professor = Professor.create_professor(professor_id=professor_id,
                                           name=name,
                                           university=generate_university,
                                           description=description,
                                           rate=rate)
    return professor


@pytest.fixture
def user_example():
    user_data = {'username': "username", 'password': "password", 'email': "user@example.com",
                 'university': "RU", 'degree': "CS"}
    user = User.create_user(*user_data)
    return user


@pytest.fixture
def generate_course(generate_degree, generate_professor, generate_university, course_id=1, name="History of Countries",
                    mandatory=True, description="Learn about historic events and their influences on countries"):
    course = Course.create_course(course_id=course_id, name=name, degree=generate_degree, mandatory=mandatory,
                                  description=description, professor=generate_professor, university=generate_university)
    course.save()
    return course


@pytest.fixture
def generate_course(generate_degree, generate_professor, generate_university, course_id=1, name="History of Countries",
                    mandatory=True, description="Learn about historic events and their influences on countries"):
    course = Course.create_course(course_id=course_id, name=name, degree=generate_degree, mandatory=mandatory,
                                  description=description, professor=generate_professor, university=generate_university)
    course.save()
    return course
