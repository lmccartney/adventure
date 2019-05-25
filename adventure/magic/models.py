from django.db import models


class Card(models.Model):
    """
    These are distinct cards that Wizards has created over the years. The union
    of this model & the Set model in Print creates the actual printings of
    the card. This added complexity is there to facilitate the tracking of
    monetary values for each printing.
    """
    name = models.CharField(max_length=64, unique=True)

class Set(models.Model):
    """
    These are the actual sets printed by Wizards.
    """
    name = models.CharField(max_length=64, unique=True)

class Print(models.Model):
    """
    The distinct printing of a card in a set
    """
    card = models.ForeignKey('magic.Card', on_delete=models.CASCADE)
    set = models.ForeignKey('magic.Set', on_delete=models.CASCADE)

