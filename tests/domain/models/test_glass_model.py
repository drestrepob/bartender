from bartender.domain.models.glass import Glass
from tests.domain.factories import GlassFactory


class TestGlassModel:
    """Test cases for Glass model."""
    def test_create_glass(self) -> None:
        glass: Glass = GlassFactory()
        assert glass.name
        assert glass.description
        assert glass.capacity
        assert glass.capacity_unit
