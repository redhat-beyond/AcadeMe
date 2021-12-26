from AcadeMe import views
from django.template.loader import render_to_string


def test_homepage(client):
    request = client.get('')
    response = views.homePage(request)
    assert response.status_code == 200


def test_homepage_html(client):
    request = client.get('')
    response = views.homePage(request)
    expected_html = render_to_string('landing/homepage.html', request=request)
    assert response.content.decode() == expected_html


def test_contactus(client):
    request = client.get('contact_us/')
    response = views.contact(request)
    assert response.status_code == 200


def test_contactus_html(client):
    request = client.get('contact_us/')
    response = views.contact(request)
    expected_html = render_to_string('landing/contact_us.html', request=request)
    assert response.content.decode() == expected_html
