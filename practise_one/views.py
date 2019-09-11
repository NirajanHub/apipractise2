# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from practise_api.practise_one.models import Article


class ArticleView(APIView):
    def get(self,request):
        articles=Article.object.all()
        return Response({"articles": articles})

