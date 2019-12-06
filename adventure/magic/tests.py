"""Testing suite for the magic app"""

from django.test import TestCase

from adventure.magic.models import Card


class MockCard:
    colors = ['Red', 'White']
    rarity = 'Rare'
    cmc = 4
    legalities = [{'format': 'Standard', 'legality': 'Legal'}, {'format': 'Vintage', 'legality': 'Restricted'}]
    name = 'Mock Card'


# noinspection PyTypeChecker
class CardFromMTGSDKCard(TestCase):
    """TestCase for Card.from_mtgsdk_card"""

    @classmethod
    def setUpTestData(cls):
        cls.card = Card.from_mtgsdk_card(MockCard)

    def test_creates_card(self):
        """first test. it fails."""
        self.assertTrue(Card.objects.filter(name='Mock Card').exists())

    def test_return_value(self):
        """Test that the returned card has the write values and is the right type"""
        self.assertIsInstance(self.card, Card)
        self.assertEqual(self.card.colors, ['Red', 'White'])
        self.assertEqual(self.card.rarity, 'Rare')
        self.assertEqual(self.card.converted_mana_cost, 4)
        self.assertTrue(self.card.standard_legal)
        self.assertTrue(self.card.vintage_legal)
        self.assertFalse(self.card.commander_legal)
        self.assertFalse(self.card.duel_legal)
        self.assertFalse(self.card.legacy_legal)
        self.assertFalse(self.card.modern_legal)
        self.assertFalse(self.card.pauper_legal)
