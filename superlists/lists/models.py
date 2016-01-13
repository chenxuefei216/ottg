from __future__ import unicode_literals

from django.db import models

# extending models.Model giving all the saving and retriving methods we need in test.py
class List(models.Model):
    pass

class Item(models.Model):
    text = models.TextField(default = '')
    # 1 (List) to many (Items) relationship (can also call it: foreign key)
    list = models.ForeignKey(List, default = None)
    is_done = models.BooleanField(default=False)
