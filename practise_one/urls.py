from django.urls import path

from practise_api.practise_one.views import ArticleView

app_name = 'practise_one'
urlpatterns = [
    path('articles/', ArticleView.as_view())
]
