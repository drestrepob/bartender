from bartender.domain.models.base import EntityId
from bartender.domain.models.glass import Glass
from tests.domain.factories import GlassFactory


class TestGlassModel:
    """Test cases for Glass model."""
    def test_create_glass(self) -> None:
        glass: Glass = GlassFactory()
        assert isinstance(glass, Glass)
        assert isinstance(glass.id, EntityId)
        assert isinstance(glass.name, str)
        assert isinstance(glass.description, str)
        assert isinstance(glass.capacity, int)
        assert isinstance(glass.capacity_unit, str)
