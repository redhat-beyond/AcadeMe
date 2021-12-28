import pytest
from AcadeMeData.models import Course
from AcadeMeData import views


@pytest.mark.django_db
def test_query(generate_course):
    assert Course.objects.filter(name__icontains=generate_course.name)[0].name == generate_course.name

@pytest.mark.django_db
def test_search(client):
    response = client.get('/search/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_search_html(client):
    response = views.SearchResultsView(client)
    assert response.content.decode() == render_to_string('search/search.html')