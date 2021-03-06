from django.db import models
from .expansion import Expansion

class Artifact(models.Model):
    name_jp_kanji = models.CharField(max_length=30)
    name_jp_pronunciations = models.CharField(max_length=30)
    name_en = models.CharField(max_length=60)
    expansion = models.ForeignKey(Expansion, on_delete=models.PROTECT)
    text_jp = models.TextField()
    text_en = models.TextField()

    class Meta:
        db_table = 'artifacts'