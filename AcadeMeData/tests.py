import pytest
from AcadeMeData.models import University


class TestUniversityModel(pytest):
    @pytest
    def test_get_university_by_id(self):
        universityTest = University.get_university_by_id(1)
        assert universityTest.exist()
