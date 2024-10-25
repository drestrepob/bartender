from dataclasses import dataclass

from domain.models.base import TimeStampedModel
from domain.models.mixins.as_dict import DictSerializerMixin


@dataclass
class User(TimeStampedModel, DictSerializerMixin):
    """Represents a user of the system."""
    username: str
    email: str
    email_verified: bool
    email_verified_at: str
    password: str
    is_active: bool
    is_superuser: bool
    is_staff: bool
    first_name: str
    last_name: str
    date_of_birth: str
    phone_number: str
    avatar: str
    bio: str