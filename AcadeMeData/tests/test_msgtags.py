import pytest
from AcadeMeData.models import MessageTags, Messages, User


@pytest.fixture
def user_example():
    user_data = {'username': "username2212", 'password': "password", 'email': "user@example.com", 'type': "S",
                 'university': "RU",
                 'degree': "CS"}
    user = User.create_user(*user_data)
    return user


@pytest.mark.django_db
class TestMessageTagsModel:
    def test_get_msg_tag(self, user_example, id=1, msgID=None):
        userID = user_example
        msgID = Messages.create_message(id, userID, text='bla bla')
        tag = MessageTags(id, msgID, userID)
        assert isinstance(tag, MessageTags)
