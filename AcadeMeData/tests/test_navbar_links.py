import pytest
from AcadeMeData.models import User


@pytest.fixture
def user_example():
    user_data = {'username': "username", 'password': "password", 'email': "user@example.com",
                 'university': "RU", 'degree': "CS"}
    user = User.create_user(*user_data)
    return user


@pytest.mark.django_db
class TestNavbarLinks:
    def navbar_links_for_logged_in_user(client, user_example):
        client.force_login(user_example.user)
        response = client.get("/")
        assert response.status_code == 200
        assert response.context['navbar_links'] == {f"Hello {user_example.user.username}": "#",
                                                    "Log Out": "/logout"}

    def navbar_links_for_not_logged_in_user(client):
        response = client.get("/")
        assert response.status_code == 200
        assert response.context['navbar_links'] == {"Log In": "/login",
                                                    "Register": "/register"}
