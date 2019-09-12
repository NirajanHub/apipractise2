# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import ArticleSerializer
from .models import Article


class ArticleView(APIView):
    def get(self, request, pk):
        articles = Article.objects.all()
        serealizer = ArticleSerializer(articles, many='true')
        return Response({"articles": serealizer.data})


    def post(self, request):
        article = request.data.get('article')
        serializer = ArticleSerializer(data=article)
        if (serializer.is_valid(raise_exception=True)):
            article_saved = serializer.save()
        return Response({"success": "Article '{}' created sucessfully".format(article_saved.title)})

    def put(self, request, pk):
        saved_article = get_object_or_404(Article.objects.all(), pk=pk)
        data = request.data.get('article')
        serializer = ArticleSerializer(instance=saved_article, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Article '{}' updated successfully".format(article_saved.title)})

    def delete(self, request, pk):
        article = get_object_or_404(Article.objects.all(), pk=pk)
        article.delete()
        return Response({"success": "Article '{}' updated successfully".format(pk)},status=204)
