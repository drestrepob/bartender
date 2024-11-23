from dataclasses import asdict, dataclass


@dataclass
class DictSerializerMixin:
    def as_dict(self):
        return asdict(self)  # noqa
