import pytest
from AcadeMeData.models import University


@pytest.mark.django_db
class TestUniversityModel:
    def test_get_university_by_name(self, generate_university, name='The Technion'):
        university_test = University.get_university_by_name(name)
        assert generate_university == university_test
        assert isinstance(university_test, University)

    def test_get_university_by_location(self, generate_university, location="Haifa"):
        university_test = University.get_university_by_location(location)
        assert generate_university == university_test
        assert isinstance(university_test, University)
