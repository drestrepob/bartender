from abc import ABC, abstractmethod

from bartender.domain.models.base import EntityId
from bartender.domain.models.glass import Glass
from bartender.domain.interfaces.repository import Repository


class GlassRepository(Repository[Glass], ABC):
    """Interface for the Glass repository."""

    @abstractmethod
    def add(self, glass: Glass) -> Glass:
        pass

    @abstractmethod
    def get(self, id_: EntityId) -> Glass:
        pass

    @abstractmethod
    def delete(self, glass: Glass) -> None:
        pass

    @abstractmethod
    def list(self) -> list[Glass]:
        pass

    @abstractmethod
    def update(self, id_: EntityId, fields: dict) -> None:
        pass
