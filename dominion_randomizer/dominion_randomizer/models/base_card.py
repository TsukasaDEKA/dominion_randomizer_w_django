from django.db import models
from .expansion import Expansion

class BaseCard(models.Model):
    name_jp_kanji = models.CharField(max_length=30)
    name_jp_pronunciations = models.CharField(max_length=30)
    name_en = models.CharField(max_length=60)
    expansion = models.ForeignKey(Expansion, on_delete=models.PROTECT)
    text_jp = models.TextField()
    text_en = models.TextField()

    # Cost
    cost_coin = models.IntegerField(null=True)
    cost_potion = models.IntegerField(null=True)
    cost_debt = models.IntegerField(null=True)

    # Gain
    gain_card = models.IntegerField(null=True)
    gain_action = models.IntegerField(null=True)
    gain_buy = models.IntegerField(null=True)
    gain_coin = models.IntegerField(null=True)
    gain_vp = models.IntegerField(null=True)
    gain_villager = models.IntegerField(null=True)
    gain_coffer = models.IntegerField(null=True)

    # Types
    types = models.CharField(max_length=60)
    action = models.BooleanField(default=False, null=True)
    attack = models.BooleanField(default=False, null=True)
    castle = models.BooleanField(default=False, null=True)
    curse = models.BooleanField(default=False, null=True)
    doom = models.BooleanField(default=False, null=True)
    duration = models.BooleanField(default=False, null=True)
    fate = models.BooleanField(default=False, null=True)
    gathering = models.BooleanField(default=False, null=True)
    heirloom = models.BooleanField(default=False, null=True)
    knight = models.BooleanField(default=False, null=True)
    night = models.BooleanField(default=False, null=True)
    looter = models.BooleanField(default=False, null=True)
    prize = models.BooleanField(default=False, null=True)
    reaction = models.BooleanField(default=False, null=True)
    reserve = models.BooleanField(default=False, null=True)
    ruins = models.BooleanField(default=False, null=True)
    spirit = models.BooleanField(default=False, null=True)
    shelter = models.BooleanField(default=False, null=True)
    treasure = models.BooleanField(default=False, null=True)
    traveller = models.BooleanField(default=False, null=True)
    victory = models.BooleanField(default=False, null=True)
    zombie = models.BooleanField(default=False, null=True)

    class Meta:
        db_table = 'base_cards'
