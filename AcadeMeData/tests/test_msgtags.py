import pytest
from AcadeMeData.models import MessageTags, Messages, User


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


<<<<<<< HEAD
@pytest.mark.django_db
class TestMessageTagsModel:
=======
@pytest.mark.django_db
class TestMessageTagsModel:
    @pytest.fixture
    def user_example(self):
        user_data = {'username': "username2212", 'password': "password", 'email': "user@example.com", 'type': "S",
                     'university': "RU",
                     'degree': "CS"}
        user = User.create_user(*user_data)
        return user

>>>>>>> 74349c9 (Seperated the tests.py file into 3 files each one contains Tests for each model class of messages. Also all of the tests are inside a new folder called Tests.)
=======
@pytest.mark.django_db
class TestMessageTagsModel:
>>>>>>> e0ebfd2 (Fixed the last fixtures review, moved them outside of classes for convenience. added some assert functions to make the tests better.)
    def test_get_msg_tag(self, user_example, id=1, msgID=None):
        userID = user_example
        msgID = Messages.create_message(id, userID, text='bla bla')
        tag = MessageTags(id, msgID, userID)
        assert isinstance(tag, MessageTags)
