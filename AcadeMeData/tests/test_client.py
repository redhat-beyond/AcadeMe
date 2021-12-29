import pytest


@pytest.mark.django_db
def test_homepage(client):
    response = client.get('')
    assert response.status_code == 200


@pytest.mark.django_db
def test_contactus(client):
    response = client.get('/contact-us/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_courselist(client):
    response = client.get('/course-list/')
    assert response.status_code == 200



