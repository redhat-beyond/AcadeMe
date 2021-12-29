import pytest
from AcadeMeData.models import Messages


@pytest.mark.django_db
class TestMessagesModel:
    def test_get_msg(generate_message):
        msg_test = Messages.get_msg_by_id(1)
        print(generate_message)
        assert not msg_test == generate_message
        assert isinstance(msg_test, Messages)

    def test_create_msg(generate_message, generate_msgboard, user_example, msgID=1, text='I am testinggggg'):
        msg = Messages.create_message(msgID, user_example, text, generate_msgboard)
        assert isinstance(msg, Messages)
        assert not generate_message == msg
        assert "I am" in msg.text
