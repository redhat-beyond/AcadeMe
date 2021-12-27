from django.template.loader import render_to_string
import pytest
from AcadeMe import views


@pytest.mark.django_db
def test_homepage_html(client):
    response = views.homePage(client)
    assert response.content.decode() == render_to_string('landing/homepage.html')


@pytest.mark.django_db
def test_contactus_html(client):
    response = views.contact(client)
    assert response.content.decode() == render_to_string('landing/contact_us.html')
