from django.db import models
from .expansion import Expansion

class Event(models.Model):
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

    class Meta:
        db_table = 'events'