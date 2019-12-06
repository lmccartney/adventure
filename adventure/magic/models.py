"""Models related to the magic app"""
from enum import Enum

from django.contrib.postgres.fields import ArrayField
from django.db import models


class Colors(Enum):
    """Valid colors in magic"""
    RED = 'Red'
    BLUE = 'Blue'
    GREEN = 'Green'
    WHITE = 'White'
    BLACK = 'Black'


class Rarity(Enum):
    """Valid rarities in magic"""
    COMMON = 'Common'
    UNCOMMON = 'Uncommon'
    RARE = 'Rare'
    MYTHIC = 'Mythic Rare'
    SPECIAL = 'Special'
    LAND = 'Basic Land'


class Card(models.Model):
    """
    These are distinct cards that Wizards has created over the years. The union
    of this model & the Set model in Print creates the actual printings of
    the card. This added complexity is there to facilitate the tracking of
    monetary values for each printing.
    """
    name = models.CharField(max_length=64, unique=True)
    converted_mana_cost = models.IntegerField()
    colors = ArrayField(
        base_field=models.CharField(
            max_length=8, choices=[(x, x.value) for x in Colors]),
    )
    rarity = models.CharField(
        max_length=16, choices=[(x, x.value) for x in Rarity]
    )
    commander_legal = models.BooleanField(default=False)
    duel_legal = models.BooleanField(default=False)
    legacy_legal = models.BooleanField(default=False)
    modern_legal = models.BooleanField(default=False)
    pauper_legal = models.BooleanField(default=False)
    standard_legal = models.BooleanField(default=False)
    vintage_legal = models.BooleanField(default=False)

    @classmethod
    def from_mtgsdk_card(cls, mtgsdk_card):
        """
        Generate an adventure.Card from an mtgsdk.Card instance
        :param mtgsdk.Card mtgsdk_card: a Card instance from the mtgsdk library
        :return: the Card
        :rtype: Card
        """
        card_defaults = {
            **{
                'colors': mtgsdk_card.colors,
                'rarity': mtgsdk_card.rarity,
                'converted_mana_cost': mtgsdk_card.cmc,
            },
            **{
                f'{x["format"].lower()}_legal': bool(x['legality'] in ['Legal', 'Restricted'])
                for x in mtgsdk_card.legalities
            }
        }
        card, _ = Card.objects.update_or_create(
            name=mtgsdk_card.name,
            defaults=card_defaults,
        )
        return card


class Set(models.Model):
    """
    These are the actual sets printed by Wizards.
    """
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=4, unique=True)


class Print(models.Model):
    """
    The distinct printing of a card in a set
    """
    card = models.ForeignKey('magic.Card', on_delete=models.CASCADE)
    set = models.ForeignKey('magic.Set', on_delete=models.CASCADE)
    artist = models.CharField(max_length=64)

    @classmethod
    def update(cls, mtgsdk_card):
        """
        Method to take a printing from the mtg sdk and update the database
        with its data.
        :param mtgsdk.Card mtgsdk_card: The printing to update
        :return: The print
        :rtype: Print
        """
        card = Card.from_mtgsdk_card(mtgsdk_card)

        set_defaults = {
            'name': mtgsdk_card.set_name,
        }
        mtg_set, _ = Set.objects.update_or_create(
            code=mtgsdk_card.set,
            defaults=set_defaults,
        )

        print_defaults = {
            'artist': mtgsdk_card.artist,
        }
        mtg_print, _ = Print.objects.update_or_create(
            card=card, set=mtg_set,
            defaults=print_defaults,
        )

        return mtg_print
