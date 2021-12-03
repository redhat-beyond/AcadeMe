import pytest
from AcadeMeData.models import Messages, User


<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e0ebfd2 (Fixed the last fixtures review, moved them outside of classes for convenience. added some assert functions to make the tests better.)
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


<<<<<<< HEAD
@pytest.mark.django_db
class TestMessagesModel:

    def test_get_msg(self, generate_message):
        msg = generate_message
=======
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
>>>>>>> 74349c9 (Seperated the tests.py file into 3 files each one contains Tests for each model class of messages. Also all of the tests are inside a new folder called Tests.)
=======
@pytest.mark.django_db
class TestMessagesModel:

    def test_get_msg(self, generate_message):
        msg = generate_message
>>>>>>> e0ebfd2 (Fixed the last fixtures review, moved them outside of classes for convenience. added some assert functions to make the tests better.)
        msg_test = Messages.get_msg_by_id(1)
        assert msg_test == msg
        assert isinstance(msg_test, Messages)

<<<<<<< HEAD
<<<<<<< HEAD
    def test_create_msg(self, generate_message, user_example, msgID=9, text='I am testinggggg'):
        user = user_example
        msg = Messages.create_message(msgID, user, text)
        msg_test = generate_message
        assert isinstance(msg, Messages)
        assert not msg_test == msg
        assert "I am" in msg.text
        assert "This" in msg_test.text
=======
    def test_create_msg(self, user_example, msgID=9, text='I am testinggggg'):
=======
    def test_create_msg(self, generate_message, user_example, msgID=9, text='I am testinggggg'):
>>>>>>> e0ebfd2 (Fixed the last fixtures review, moved them outside of classes for convenience. added some assert functions to make the tests better.)
        user = user_example
        msg = Messages.create_message(msgID, user, text)
        msg_test = generate_message
        assert isinstance(msg, Messages)
<<<<<<< HEAD
>>>>>>> 74349c9 (Seperated the tests.py file into 3 files each one contains Tests for each model class of messages. Also all of the tests are inside a new folder called Tests.)
=======
        assert not msg_test == msg
        assert "I am" in msg.text
        assert "This" in msg_test.text
>>>>>>> e0ebfd2 (Fixed the last fixtures review, moved them outside of classes for convenience. added some assert functions to make the tests better.)
