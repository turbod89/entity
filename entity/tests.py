import uuid
import dataclasses
from unittest import TestCase
from .entity import Entity
from .entity_pool import __entity_pool__
from .exceptions import EntityNotFoundException


class EntityModelWeakRefTestCase(TestCase):

    def test_001(self):
        """Test entity is saved in dict"""
        entity = Entity()
        self.assertEqual(len(__entity_pool__.entity_pool), 1)
        self.assertIn(entity.uuid, __entity_pool__.entity_pool)
        self.assertEqual(__entity_pool__.entity_pool.get(entity.uuid), entity)

    def test_002(self):
        """Test entity is removed from dict on delete"""
        entity = Entity()
        self.assertEqual(len(__entity_pool__.entity_pool), 1)
        del entity
        self.assertEqual(len(__entity_pool__.entity_pool), 0)

    def test_003(self):
        """Test entity is re-keyed in dict at uuid update"""
        entity = Entity()
        old_uuid = entity.uuid
        self.assertEqual(len(__entity_pool__.entity_pool), 1)
        self.assertIn(old_uuid, __entity_pool__.entity_pool)
        new_uuid = uuid.uuid4()
        entity.uuid = new_uuid
        self.assertNotEqual(old_uuid, entity.uuid)
        self.assertEqual(len(__entity_pool__.entity_pool), 1)
        self.assertIn(new_uuid, __entity_pool__.entity_pool)
        self.assertNotIn(old_uuid, __entity_pool__.entity_pool)


class EntityModelTestCase(TestCase):

    def test_001(self):
        """Test entity can be obtained with the uuid"""

        @dataclasses.dataclass
        class A(Entity):
            a: str = dataclasses.field(default='')

        a = A()
        b = A.get(a.uuid)
        self.assertEqual(a, b)
        c = A.get(a.uuid)
        self.assertEqual(a, c)

    def test_002(self):
        """Test EntityNotFoundException is raised if get an invalid uuid"""

        with self.assertRaises(EntityNotFoundException):
            Entity.get(uuid.uuid4())
