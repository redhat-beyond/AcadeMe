import pytest
from AcadeMeData.models import University


class TestUniversityModel(pytest):
    @pytest
    def test_get_university_by_name(self):
        universityTest = University.get_university_by_name(
            'Reichman University')
        assert universityTest.exist()

    @pytest
    def test_get_university_by_location(self):
        universityTest = University.get_university_by_location(
            'Jerusalem')
        assert universityTest.exist()
