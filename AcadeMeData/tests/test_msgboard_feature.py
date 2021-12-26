import pytest
from AcadeMeData.models import MessageBoards, Course, Degree, Professor, User
from AcadeMeData.forms import MessageForm


@pytest.fixture
def user_example():
    user_data = {'username': "username2212", 'password': "password", 'email': "user@example.com",
                 'university': "RU",
                 'degree': "CS"}
    user = User.create_user(*user_data)
    return user


@pytest.mark.django_db
def test_msgboard_feature(client, user_example):
    client.force_login(user_example.user)
    response = client.get("/msgboard/")
    assert response.status_code == 200
    form = response.context["form"]
    assert isinstance(form, MessageForm)
