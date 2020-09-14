import weakref
from uuid import UUID
from typing import Optional
from .exceptions import EntityNotFoundException


class EntityPool(object):
    def get(self, uuid: UUID):
        cls_name = type(self).__name__
        raise NotImplementedError(
            f'Class {cls_name} has no method `get` implemented.'
        )

    def set(self, uuid: UUID, value):
        cls_name = type(self).__name__
        raise NotImplementedError(
            f'Class {cls_name} has no method `set` implemented.'
        )

    def pop(self, uuid: UUID, default=None):
        cls_name = type(self).__name__
        raise NotImplementedError(
            f'Class {cls_name} has no method `pop` implemented.'
        )


class WeakValueDictionaryEntityPool(EntityPool):
    def __init__(
        self,
        entity_pool: Optional[weakref.WeakValueDictionary] = None
    ):
        self.entity_pool = entity_pool or weakref.WeakValueDictionary()

    def get(self, uuid: UUID):
        try:
            return self.entity_pool[uuid]
        except KeyError:
            raise EntityNotFoundException

    def set(self, uuid: UUID, value):
        self.entity_pool[uuid] = value

    def pop(self, uuid: UUID, default=None):
        return self.entity_pool.pop(uuid, default)


__entity_pool__ = WeakValueDictionaryEntityPool()


def setEntityTool(entity_pool: EntityPool):
    global __entity_pool__
    __entity_pool__ = entity_pool


__all__ = (
    'WeakValueDictionaryEntityPool',
    'setEntityTool',
    'EntityPool',
    '__entity_pool__',
)
