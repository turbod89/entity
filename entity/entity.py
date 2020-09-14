import dataclasses
from uuid import UUID, uuid4
from .entity_pool import __entity_pool__
from .exceptions import EntityNotFoundException


@dataclasses.dataclass
class Entity(object):
    uuid: UUID = dataclasses.field(default_factory=uuid4)

    def __new__(cls, *args, **kwargs):
        try:
            instance = cls.get(kwargs.get('uuid'))
        except EntityNotFoundException:
            instance = super().__new__(cls)
            instance.__init__(*args, **kwargs)
            return instance

    def __setattr__(self, name, value):

        if name == 'uuid':
            if not isinstance(value, UUID):
                raise ValueError('badly formed hexadecimal UUID string')

            if hasattr(self, name):
                __entity_pool__.pop(getattr(self, name), None)

        super().__setattr__(name, value)

        if name == 'uuid':
            __entity_pool__.set(value, self)

    def to_dict(self):
        return {
            'uuid': str(self.uuid)
        }

    @classmethod
    def get(cls, uuid: UUID):
        return __entity_pool__.get(uuid)

    @classmethod
    def from_dict(cls, data):
        return Entity.get(UUID(data.get('uuid'))) or Entity(**data)


__all__ = (
    'Entity',
)
