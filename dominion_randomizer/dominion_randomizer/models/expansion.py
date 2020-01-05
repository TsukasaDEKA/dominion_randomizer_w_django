from django.db import models

class Expantion(models.Model):
    name_jp_kanji = models.CharField(max_length=30)
    name_jp_pronunciations = models.CharField(max_length=30)
    name_en = models.CharField(max_length=60)

    class Meta:
        db_table = 'expantions'