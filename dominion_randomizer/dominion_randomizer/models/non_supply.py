from django.db import models
from .expansion import Expantion

class NonSupply(models.Model):
    name_jp_kanji = models.CharField(max_length=30)
    name_jp_pronunciations = models.CharField(max_length=30)
    name_en = models.CharField(max_length=60)
    expansion = models.ForeignKey(Expantion, on_delete=models.PROTECT)
    text_jp = models.TextField()
    text_en = models.TextField()

    # Cost
    cost_coin = models.IntegerField()
    cost_potion = models.IntegerField()
    cost_debt = models.IntegerField()

    # Gain
    gain_card = models.IntegerField()
    gain_action = models.IntegerField()
    gain_buy = models.IntegerField()
    gain_money = models.IntegerField()
    gain_vp = models.IntegerField()
    gain_villager = models.IntegerField()
    gain_coffer = models.IntegerField()


    # Types
    types = models.CharField(max_length=60)
    action = models.BooleanField(default=False)
    attack = models.BooleanField(default=False)
    castle = models.BooleanField(default=False)
    doom = models.BooleanField(default=False)
    duration = models.BooleanField(default=False)
    fate = models.BooleanField(default=False)
    gathering = models.BooleanField(default=False)
    heirloom = models.BooleanField(default=False)
    knight = models.BooleanField(default=False)
    night = models.BooleanField(default=False)
    reaction = models.BooleanField(default=False)
    ruins = models.BooleanField(default=False)
    spirit = models.BooleanField(default=False)
    shelter = models.BooleanField(default=False)
    treasure = models.BooleanField(default=False)
    victory = models.BooleanField(default=False)
    zombie = models.BooleanField(default=False)

    class Meta:
        db_table = 'non_supplies'