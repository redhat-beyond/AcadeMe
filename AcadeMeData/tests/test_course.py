import pytest
from AcadeMeData.models import Course, Degree


@pytest.fixture
def generate_course(generate_degree, generate_professor, generate_university, course_id=1, name="History of Countries",
                    mandatory=True, description="Learn about historic events and their influences on countries"):
    course = Course.create_course(course_id=course_id, name=name, degree=generate_degree, mandatory=mandatory,
                                  description=description, professor=generate_professor, university=generate_university)
    course.save()
    return course


@pytest.fixture
def generate_degree_that_dosent_have_course(degree_id=5, name='Computer Science', universities="Reichman University",
                                            description="Learn to be a programmer"):
    """This degree doesnt include the course defined in generate_course"""
    degree = Degree.create_degree(degree_id=degree_id, name=name, universities=universities,
                                  description=description)
    degree.save()
    return degree


@pytest.mark.django_db
class TestCourseModel:
    def test_get_course_by_name(self, generate_course, name="History of Countries"):
        course = Course.get_course_by_name(name)
        assert course.name == generate_course.name
        assert course.professor == generate_course.professor

    def test_if_course_belongs(self, generate_course, generate_degree, generate_university):
        assert generate_course.course_belongs(generate_university, generate_degree)

    def test_if_course_not_belongs(self, generate_course, generate_university):
        assert not generate_course.course_belongs(generate_university, generate_degree_that_dosent_have_course)
