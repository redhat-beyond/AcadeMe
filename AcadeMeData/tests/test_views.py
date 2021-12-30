from pytest_django.asserts import assertTemplateUsed
import pytest


@pytest.mark.django_db
def test_homepage_html(client, user_example, generate_all_degree_set, generate_all_university_set):
    client.force_login(user_example.user)
    response = client.get("")
    assertTemplateUsed(response, 'landing/homepage.html')
    assert response.context['navbar_links'] == {f"Welcome {user_example.user.username}": "#",
                                                "Logout": "/logout"}
    assert set(response.context['all_universities']) == generate_all_university_set
    assert set(response.context['all_degrees']) == generate_all_degree_set


@pytest.mark.django_db
def test_contactus_html(client, user_example):
    client.force_login(user_example.user)
    response = client.get("/contact_us/")
    assertTemplateUsed(response, 'landing/contact_us.html')
    assert response.context['navbar_links'] == {f"Welcome {user_example.user.username}": "#",
                                                "Logout": "/logout"}


@pytest.mark.django_db
def test_courselist_html(client, user_example, generate_all_courses_set):
    client.force_login(user_example.user)
    response = client.post("/course-list/",
                           {'selectUniversity': 'Reichman University', 'selectDegree': 'Computer Science'})
    assertTemplateUsed(response, 'landing/course-list-page.html')
    assert response.context['navbar_links'] == {f"Welcome {user_example.user.username}": "#",
                                                "Logout": "/logout"}
    assert response.context['seluniversity'] == 'Reichman University'
    assert response.context['seldegree'] == 'Computer Science'
    assert set(response.context['all_courses']) == generate_all_courses_set
