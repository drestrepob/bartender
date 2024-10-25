from bartender.domain.models.tag import Tag
from tests.domain.factories import TagFactory


class TestTagModel:
    """Test cases for Tag model."""
    def test_create_tag(self) -> None:
        tag: Tag = TagFactory()
        assert tag.name
        assert tag.created_at
        assert tag.updated_at
