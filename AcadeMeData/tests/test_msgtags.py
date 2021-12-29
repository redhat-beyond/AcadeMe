import pytest
from AcadeMeData.models import MessageTags, Messages, User


@pytest.fixture
def user_example():
    user_data = {'username': "username22123", 'password': "password", 'email': "user@example.com",
                 'university': "RU",
                 'degree': "CS"}
    user = User.create_user(*user_data)
    return user


@pytest.fixture
def generate_message(user_example, msgID=10, text='This is a test message yo'):
    message = Messages(msgID=msgID, userID=user_example, text=text)
    message.save()
    return message


@pytest.fixture
def generate_msgtags(user_example, generate_message, id=1):
    tag = MessageTags.create_msgtag(id, generate_message, user_example)
    return tag


@pytest.mark.django_db
class TestMessageTagsModel:
    def test_get_msg_tag(self, generate_msgtags):
        tag_test = MessageTags.get_msg_tag(1)
        assert generate_msgtags == tag_test
        assert isinstance(generate_msgtags, MessageTags)
