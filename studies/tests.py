import pytest
from studies.models import University


@pytest.mark.django_db
class TestUniversityModel:
    @pytest.fixture
    def generate_university(self, university_id=1, name='Reichman University', location="Herzlia",
                            description="A nice place"):
        university = University(university_id=university_id, name=name, location=location,
                                description=description)
        university.save()
        return university

    def test_get_university_by_name(self, generate_university, name='Reichman University'):
        university_test = University.get_university_by_name(name)
        assert generate_university == university_test
        assert isinstance(university_test, University)

    def test_get_university_by_location(self, generate_university, location="Herzlia"):
        university_test = University.get_university_by_location(location)
        assert generate_university == university_test
        assert isinstance(university_test, University)
