import pytest
from AcadeMeData.models import Messages, User


@pytest.fixture
def user_example():
    user_data = {'username': "username2212", 'password': "password", 'email': "user@example.com", 'type': "S",
                 'university': "RU",
                 'degree': "CS"}
    user = User.create_user(*user_data)
    return user


@pytest.fixture
def generate_message(user_example, msgID=1, text='This is a test message yo'):
    user = user_example
    message = Messages(msgID=msgID, userID=user, text=text)
    message.save()
    return message


@pytest.mark.django_db
class TestMessagesModel:

    def test_get_msg(self, generate_message):
        msg = generate_message
        msg_test = Messages.get_msg_by_id(1)
        assert msg_test == msg
        assert isinstance(msg_test, Messages)

    def test_create_msg(self, generate_message, user_example, msgID=9, text='I am testinggggg'):
        user = user_example
        msg = Messages.create_message(msgID, user, text)
        msg_test = generate_message
        assert isinstance(msg, Messages)
        assert not msg_test == msg
        assert "I am" in msg.text
        assert "This" in msg_test.text
