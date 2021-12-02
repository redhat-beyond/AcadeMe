import pytest
from AcadeMeData.models import Messages, User


@pytest.mark.django_db
class TestMessagesModel:
    @pytest.fixture
    def user_example(self):
        user_data = {'username': "username2212", 'password': "password", 'email': "user@example.com", 'type': "S",
                     'university': "RU",
                     'degree': "CS"}
        user = User.create_user(*user_data)
        return user

    def generate_message(self, msgID=1, userID=None, text='This is a test message yo'):
        message = Messages(msgID=msgID, userID=userID, text=text)
        message.save()
        return message

    def test_get_msg(self, user_example, msgID=1, userID=None, text='This is a test message yo'):
        userID = user_example
        msg = TestMessagesModel.generate_message(self, msgID, userID, text)
        msg_test = Messages.get_msg_by_id(1)
        assert msg_test == msg
        assert isinstance(msg_test, Messages)

    def test_create_msg(self, user_example, msgID=9, text='I am testinggggg'):
        user = user_example
        msg = Messages.create_message(msgID, user, text)
        assert isinstance(msg, Messages)
