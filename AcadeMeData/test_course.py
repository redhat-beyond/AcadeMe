import pytest
from AcadeMeData.models import Course


@pytest.fixture
def generate_course(generate_degree, generate_professor, course_id=1, name="History of Countries",
                    elective=True, description="Learn about historic events and their influences on countries"):
    professor = generate_professor
    degree = generate_degree
    course = Course.create_course(course_id=course_id, name=name, degree=degree, elective=elective,
                                  description=description, professor=professor)
    course.save()
    return course


@pytest.mark.django_db
class TestCourseModel:
    def test_create_course(self, generate_course, name="History of Countries"):
        course = Course.get_course_by_name(name)

        assert course.name == generate_course.name
        assert course.professor == generate_course.professor
