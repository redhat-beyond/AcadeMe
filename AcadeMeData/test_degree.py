import pytest
from AcadeMeData.models import Degree


@pytest.mark.django_db
class TestDegreeModel:
    def degree_example(self):
        degree = Degree(degree_id=1, name='History', universities="Reichman University",
                        description="Learn about historic events and their influences on the world")
        degree.save()
        return degree

    def test_create_degree(self, degree_id=1, name="History",
                           universities="Reichman University, Ben Gurion University",
                           description="Learn about historic events and their influences on the world"):
        degree_test = Degree.create_degree(degree_id=degree_id, name=name, universities=universities,
                                           description=description)
        assert "Reichman University" in degree_test.universities
        assert degree_test.name == "History"
