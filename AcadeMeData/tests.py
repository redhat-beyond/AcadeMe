import pytest
from AcadeMeData.models import Degree


@pytest
class TestDegreeModel(pytest):
    def test_get_name(self):
        test_degree = Degree(degree='Computer Science').save()
        assert test_degree.get_name() == 'Reichman University'

    def test_universities(self):
        test_degree = Degree(degree='Economics', universities='Reichman University').save()
        assert "Reichman University" in test_degree.universities()
