from pytest_django.asserts import assertTemplateUsed
import pytest
from AcadeMeData.models import University, Degree


@pytest.mark.django_db
def test_homepage_html(client, user_example):
    all_universities = University.objects.all()
    all_degrees = Degree.objects.all()
    client.force_login(user_example.user)
    response = client.get("")
    assertTemplateUsed(response, 'landing/homepage.html')
    assert response.context['navbar_links'] == {f"Welcome {user_example.user.username}": "#",
                                                "Logout": "/logout"}
    assert set(response.context['all_universities']) == set(all_universities)
    assert set(response.context['all_degrees']) == set(all_degrees)


@pytest.mark.django_db
def test_contactus_html(client, user_example):
    client.force_login(user_example.user)
    response = client.get("/contact_us/")
    assertTemplateUsed(response, 'landing/contact_us.html')
    assert response.context['navbar_links'] == {f"Welcome {user_example.user.username}": "#",
                                                "Logout": "/logout"}
