from dataclasses import dataclass

from bartender.domain.models.base import BaseModel
from bartender.domain.models.mixins.as_dict import DictSerializerMixin


@dataclass(slots=True)
class User(BaseModel, DictSerializerMixin):
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
