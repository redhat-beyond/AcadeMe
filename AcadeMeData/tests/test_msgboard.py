import pytest
from AcadeMeData.models import MessageBoards


<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e0ebfd2 (Fixed the last fixtures review, moved them outside of classes for convenience. added some assert functions to make the tests better.)
=======
>>>>>>> e0ebfd2 (Fixed the last fixtures review, moved them outside of classes for convenience. added some assert functions to make the tests better.)
@pytest.fixture
def generate_msgboard(id=1, courseName="Linear Algebra"):
    msgboard = MessageBoards(id=id, courseName=courseName)
    msgboard.save()
    return msgboard


<<<<<<< HEAD
<<<<<<< HEAD
@pytest.mark.django_db
class TestMessageBoardModel:
=======
=======
>>>>>>> 74349c9 (Seperated the tests.py file into 3 files each one contains Tests for each model class of messages. Also all of the tests are inside a new folder called Tests.)
@pytest.mark.django_db
class TestMessageBoardModel:
    @pytest.fixture
    def generate_msgboard(self, id=1, courseName="Linear Algebra"):
        msgboard = MessageBoards(id=id, courseName=courseName)
        msgboard.save()
        return msgboard

<<<<<<< HEAD
>>>>>>> 74349c9 (Seperated the tests.py file into 3 files each one contains Tests for each model class of messages. Also all of the tests are inside a new folder called Tests.)
=======
@pytest.mark.django_db
class TestMessageBoardModel:
>>>>>>> e0ebfd2 (Fixed the last fixtures review, moved them outside of classes for convenience. added some assert functions to make the tests better.)
=======
>>>>>>> 74349c9 (Seperated the tests.py file into 3 files each one contains Tests for each model class of messages. Also all of the tests are inside a new folder called Tests.)
=======
@pytest.mark.django_db
class TestMessageBoardModel:
>>>>>>> e0ebfd2 (Fixed the last fixtures review, moved them outside of classes for convenience. added some assert functions to make the tests better.)
    def test_get_msgboard(self, generate_msgboard):
        msgboard = generate_msgboard
        msgboard_test = MessageBoards.get_msgboard_by_id(1)
        assert msgboard_test == msgboard
        assert isinstance(msgboard_test, MessageBoards)
