import pytest
from AcadeMeData.models import User
from AcadeMeData.forms import MessageForm
from django.contrib.messages import get_messages


@pytest.mark.django_db
def test_msgboard_login(client, user_example):
    client.force_login(user_example.user)
    response = client.get("/msgboard/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_msgboard_form_instance(client, user_example):
    client.force_login(user_example.user)
    response = client.get("/msgboard/")
    form = response.context["form"]
    assert isinstance(form, MessageForm)


@pytest.mark.django_db
def test_msgboard_empty_message_when_page_loads(client, user_example):
    client.force_login(user_example.user)
    response = client.get("/msgboard")
    messages = list(get_messages(response.wsgi_request))
    assert len(messages) == 0


@pytest.mark.django_db
def test_msgboard_feature(client, user_example, generate_msgboard):
    client.force_login(user_example.user)
    form_data = {'text': 'Lorem Ipsum',
                 'userID': user_example.user,
                 'board': generate_msgboard}
    form = MessageForm(data=form_data)
    response = client.post("/msgboard/", form_data)
    assert (form.is_valid())
    messages = list(response.context['messages'][0].text)
    assert len(messages) > 0
