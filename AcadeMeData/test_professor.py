import pytest
from AcadeMeData.models import Professor, University


@pytest.mark.django_db
class TestProfessorModel:
    @pytest.fixture
    def generate_university(self, university_id=3, name='The Hebrew University', location="Jerusalem",
                            description="good vibes"):
        university = University(university_id=university_id, name=name, location=location,
                                description=description)
        university.save()
        return university

    @pytest.fixture
    def generate_professor(self, generate_university, professor_id=2, name="DR Arnold Schwarzenegger",
                           description="A cool guy who looked familiar", rate=4.5):
        university = generate_university
        professor = Professor.create_professor(professor_id=professor_id,
                                               name=name,
                                               university=university,
                                               description=description,
                                               rate=rate)
        return professor

    def test_get_name(self, generate_professor, name="DR Arnold Schwarzenegger"):
        assert generate_professor.get_name() == name

    def test_get_professor(self, generate_professor, name="DR Arnold Schwarzenegger"):
        assert generate_professor == Professor.get_professor(name)

    def test_create_professor(self, generate_professor, name="DR Arnold Schwarzenegger"):
        professor = Professor.get_professor(name)
        assert professor.get_name() == generate_professor.name
        assert professor.get_description() == generate_professor.description