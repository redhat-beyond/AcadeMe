import pytest
from AcadeMeData.models import Degree


@pytest.mark.django_db
class TestDegreeModel:
    def test_create_degree(self, generate_degree, name="History101"):
        degree = Degree.get_degree_by_name(name)
        assert degree.name == generate_degree.name
        assert degree.universities == generate_degree.universities
