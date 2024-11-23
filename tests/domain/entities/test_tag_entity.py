from bartender.domain.models.base import EntityId
from bartender.domain.models.tag import Tag
from tests.domain.factories import TagFactory


class TestTagModel:
    """Test cases for Tag model."""
    def test_create_tag(self) -> None:
        tag: Tag = TagFactory()
        assert isinstance(tag, Tag)
        assert isinstance(tag.id, EntityId)
        assert isinstance(tag.name, str)
