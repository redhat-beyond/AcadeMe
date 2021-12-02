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
        degree_1 = self.generate_degree()
        degree_2 = Degree.get_degree_by_name("History")

        assert degree_1 == degree_2
        asset degree_1.name == "History"
