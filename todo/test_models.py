from django.test import TestCase
from .models import Item


class TestModels(TestCase):

    def test_done_default_to_false(self):
        item = Item.objects.create(name= 'test todo item')
        self.assertFalse(item.done)
