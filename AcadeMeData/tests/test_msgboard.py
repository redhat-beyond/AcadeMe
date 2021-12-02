import pytest
from AcadeMeData.models import MessageBoards


@pytest.mark.django_db
class TestMessageBoardModel:
    @pytest.fixture
    def generate_msgboard(self, id=1, courseName="Linear Algebra"):
        msgboard = MessageBoards(id=id, courseName=courseName)
        msgboard.save()
        return msgboard

    def test_get_msgboard(self, generate_msgboard):
        msgboard = generate_msgboard
        msgboard_test = MessageBoards.get_msgboard_by_id(1)
        assert msgboard_test == msgboard
        assert isinstance(msgboard_test, MessageBoards)
