import pytest


@pytest.mark.django_db
def test_homepage(client):
    response = client.get('')
    assert response.status_code == 200


@pytest.mark.django_db
def test_contactus(client):
    request = client.get('contact-us/')
    response = views.contact(request)
    assert response.status_code == 200
