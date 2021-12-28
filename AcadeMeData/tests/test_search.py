import pytest
from AcadeMeData.models import Course
from AcadeMeData import views
from django.urls import reverse


@pytest.mark.django_db
def test_query(generate_course):
    assert Course.objects.filter(name__icontains=generate_course.name)[0].name == generate_course.name


@pytest.mark.django_db
def test_search(client, generate_course):
    url = '{url}?{filter}={value}'.format(url=reverse('search'),filter='q', value=generate_course.name)
    response = client.get(url)
    assert response.status_code == 200
