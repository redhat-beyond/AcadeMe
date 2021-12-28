import pytest


@pytest.mark.django_db
def test_navbar_links_for_logged_in_user(client, user_example):
    client.force_login(user_example.user)
    response = client.get("")
    assert response.status_code == 200
    assert response.context['navbar_links'] == {f"Welcome {user_example.user.username}": "#",
                                                "Logout": "/logout"}


@pytest.mark.django_db
def test_navbar_links_for_not_logged_in_user(client):
    response = client.get("")
    assert response.status_code == 200
    assert response.context['navbar_links'] == {"Login": "/login",
                                                "Register": "/register"}
