import pytest
from AcadeMeData.models import MessageBoards


<<<<<<< HEAD
@pytest.fixture
def generate_msgboard(id=1, courseName="Linear Algebra"):
    msgboard = MessageBoards(id=id, courseName=courseName)
    msgboard.save()
    return msgboard


@pytest.mark.django_db
class TestMessageBoardModel:
=======
@pytest.mark.django_db
class TestMessageBoardModel:
    @pytest.fixture
    def generate_msgboard(self, id=1, courseName="Linear Algebra"):
        msgboard = MessageBoards(id=id, courseName=courseName)
        msgboard.save()
        return msgboard

>>>>>>> 74349c9 (Seperated the tests.py file into 3 files each one contains Tests for each model class of messages. Also all of the tests are inside a new folder called Tests.)
    def test_get_msgboard(self, generate_msgboard):
        msgboard = generate_msgboard
        msgboard_test = MessageBoards.get_msgboard_by_id(1)
        assert msgboard_test == msgboard
        assert isinstance(msgboard_test, MessageBoards)
