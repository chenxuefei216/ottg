from __future__ import unicode_literals

from django.db import models

# extending models.Model giving all the saving and retriving methods we need in test.py
class Item(models.Model):
    text = models.TextField(default = "")
