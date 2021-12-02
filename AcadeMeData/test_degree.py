import pytest
from AcadeMeData.models import Degree


@pytest.mark.django_db
class TestDegreeModel:
    @pytest.fixture
    def generate_degree(self, degree_id=1, name='History', universities="Ben Gurion University, Reichman University",
                        description="Learn about historic events and their influences on the world"):
        degree = Degree(degree_id=degree_id, name=name, universities=universities,
                        description=description)
        degree.save()
        return degree

    def test_create_degree(self, generate_degree):
        degree = Degree.create_degree(degree_id=1, name='History',
                                      universities="Ben Gurion University, Reichman University",
                                      description="Learn about historic events and their influences on the world")

        assert degree.name == generate_degree.name
        assert degree.universities == generate_degree.universities
