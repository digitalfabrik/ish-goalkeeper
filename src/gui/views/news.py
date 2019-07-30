"""
View for displaying news.
"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..models import News


@login_required
def show_news(request):
    """
    Show latest 5 news entries.
    """
    news_list = News.objects.all()  # pylint: disable=E1101
    context = {'news_list': news_list}
    return render(request, 'news.html', context)
