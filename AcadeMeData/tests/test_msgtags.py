import pytest
from AcadeMeData.models import MessageTags


@pytest.mark.django_db
class TestMessageTagsModel:
    def test_get_msg_tag(self, generate_msgtags):
        tag_test = MessageTags.get_msg_tag(1)
        assert generate_msgtags == tag_test
        assert isinstance(generate_msgtags, MessageTags)
