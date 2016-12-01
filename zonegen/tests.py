"""Django Tests"""
from django.test import TestCase
from zonegen.models import Zone

class ZoneTestCase(TestCase):
    """A placeholder test"""
    def setUp(self):
        Zone.objects.create(name="Business district", code="Bz")

    def test_thing(self):
        """Zone name"""
        zone = Zone.objects.get(code="Bz")
        self.assertEqual(zone.name, "Business district")
