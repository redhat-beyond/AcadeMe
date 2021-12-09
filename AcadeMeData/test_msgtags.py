import pytest
from AcadeMeData.models import MessageTags, Messages, User


@pytest.fixture
def user_example():
    user_data = {'username': "username2212", 'password': "password", 'email': "user@example.com",
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


@pytest.fixture
def generate_msgtags(id=1):
    tag = MessageTags(id, generate_message, user_example)
    return tag


@pytest.mark.django_db
class TestMessageTagsModel:
    def test_get_msg_tag(self, generate_msgtags):
        tag = generate_msgtags
        tag_test = MessageTags.get_msg_tag(1)
        assert tag == tag_test
        assert isinstance(tag, MessageTags)
