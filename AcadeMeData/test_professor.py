import pytest
from AcadeMeData.models import Professor


@pytest.fixture
def generate_professor(generate_university, professor_id=2, name="DR Arnold Schwarzenegger",
                       description="A cool guy who looked familiar", rate=4.5):
    university = generate_university
    professor = Professor.create_professor(professor_id=professor_id,
                                           name=name,
                                           university=university,
                                           description=description,
                                           rate=rate)
    return professor


@pytest.mark.django_db
class TestProfessorModel:
    def test_get_name(self, generate_professor, name="DR Arnold Schwarzenegger"):
        assert generate_professor.get_name() == name

    def test_get_professor(self, generate_professor, name="DR Arnold Schwarzenegger"):
        assert generate_professor == Professor.get_professor(name)

    def test_create_professor(self, generate_professor, name="DR Arnold Schwarzenegger"):
        professor = Professor.get_professor(name)
        assert professor.get_name() == generate_professor.name
        assert professor.get_description() == generate_professor.description
