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

    def test_create_degree(self):
        degree = Degree.create_degree(self, degree_id=1, name="History",
                               universities="Reichman University, Ben Gurion University",
                               description="Learn about historic events and their influences on the world")

        assert "Reichman University" in degree.get_universities()
        assert "History" in degree.get_name
        assert "historic" in degree.get_description()
