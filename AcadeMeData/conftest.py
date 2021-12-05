import pytest
from AcadeMeData.models import University


@pytest.fixture(scope="session")
def generate_university(university_id=5, name='The Technion', location="Haifa",
                        description="Best University in Israel"):
    university = University(university_id=university_id, name=name, location=location,
                            description=description)
    university.save()
    return university

