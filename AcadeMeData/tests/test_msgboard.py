import pytest
from AcadeMeData.models import MessageBoards


@pytest.fixture
def generate_msgboard(id=1):
    msgboard = MessageBoards(id=id, courseName="Linear Algebra")
    msgboard.save()
    return msgboard


@pytest.mark.django_db
class TestMessageBoardModel:
    def test_create_msgboard(self, generate_msgboard):
        assert isinstance(generate_msgboard, MessageBoards)

    def test_get_msgboard(self, generate_msgboard):
        board_test = MessageBoards.get_msgboard_by_id(1)
        assert generate_msgboard == board_test
