# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    body = models.TextField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
