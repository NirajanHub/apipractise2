# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from practise_api.practise_one.models import Article, Author

admin.site.register(Article)
admin.site.register(Author)