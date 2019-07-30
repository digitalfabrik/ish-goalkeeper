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
    # pylint: disable=E1101
    news_list = News.objects.all().order_by("-pub_date")[0:5]
    context = {'news_list': news_list}
    return render(request, 'news.html', context)
