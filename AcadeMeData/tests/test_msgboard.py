import pytest
from AcadeMeData.models import MessageBoards


@pytest.fixture
def generate_msgboard(id=1, courseName="Linear Algebra"):
    msgboard = MessageBoards(id=id, courseName=courseName)
    msgboard.save()
    return msgboard


@pytest.mark.django_db
class TestMessageBoardModel:
    @pytest.fixture
    def generate_msgboard(self, id=1, courseName="Linear Algebra"):
        msgboard = MessageBoards(id=id, courseName=courseName)
        msgboard.save()
        return msgboard
