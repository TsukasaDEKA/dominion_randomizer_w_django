from django.db import models
from .expansion import Expantion

class Event(models.Model):
    text = models.TextField()
    expansion = models.ForeignKey(Expantion, on_delete=models.PROTECT)
    name_jp_kanji = models.CharField(max_length=30)
    name_jp_pronunciations = models.CharField(max_length=30)
    name_en = models.CharField(max_length=60)

    class Meta:
        db_table = 'events'