import pytest
from AcadeMeData.models import Messages, User


@pytest.fixture
def user_example():
    user_data = {'username': "username2212", 'password': "password", 'email': "user@example.com",
                 'university': "RU",
                 'degree': "CS"}
    user = User.create_user(*user_data)
    return user


@pytest.fixture
def generate_message(user_example, msgID=1, text='This is a test message yo'):
    message = Messages(msgID=msgID, userID=user_example, text=text)
    message.save()
    return message


@pytest.mark.django_db
class TestMessagesModel:

    def test_get_msg(self, generate_message):
        msg_test = Messages.get_msg_by_id(1)
        assert msg_test == generate_message
        assert isinstance(msg_test, Messages)

    def test_create_msg(self, generate_message, user_example, msgID=9, text='I am testinggggg'):
        msg = Messages.create_message(msgID, user_example, text)
        assert isinstance(msg, Messages)
        assert not generate_message == msg
        assert "I am" in msg.text
        assert "This" in generate_message.text
