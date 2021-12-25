import pytest
from AcadeMeData.models import Course


@pytest.fixture
def generate_course(generate_degree, generate_professor, generate_university, course_id=1, name="History of Countries",
                    mandatory=True, description="Learn about historic events and their influences on countries"):
    course = Course.create_course(course_id=course_id, name=name, degree=generate_degree, mandatory=mandatory,
                                  description=description, professor=generate_professor, university=generate_university)
    course.save()
    return course


@pytest.mark.django_db
class TestCourseModel:
    def test_get_course_by_name(self, generate_course, name="History of Countries"):
        course = Course.get_course_by_name(name)
        assert course.name == generate_course.name
        assert course.professor == generate_course.professor

    def test_if_course_belongs(self, generate_course, generate_degree, generate_university):
        bool = generate_course.course_belongs(generate_university, generate_degree)
        assert bool

    def test_if_course_not_belongs(self, generate_course, generate_university):
        bool = generate_course.course_belongs(generate_university, None)
        assert not bool
