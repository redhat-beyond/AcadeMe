import pytest
from AcadeMeData.models import Course


@pytest.fixture
def generate_course(generate_degree, generate_professor, course_id=1, name="History of Countries",
                    mandatory=True, description="Learn about historic events and their influences on countries"):
    professor = generate_professor
    degree = generate_degree
    course = Course.create_course(course_id=course_id, name=name, degree=degree, mandatory=mandatory,
                                  description=description, professor=professor)
    course.save()
    return course


@pytest.mark.django_db
def test_query(generate_course):
    assert Course.objects.filter(name__icontains=generate_course.name)[0].name == generate_course.name
