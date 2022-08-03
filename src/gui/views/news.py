"""
View for displaying news.
"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..models import News


@login_required
def show_news(request, news_id=None):
    """
    Show latest 5 news entries.
    """
    # pylint: disable=E1101
    if news_id is None:
        news_list = (News.objects.filter(groups__in=request.user.groups.all())
                     .order_by("-pub_date")[0:5])
    else:
        news_list = News.objects.filter(id=news_id,groups__in=request.user.groups.all())
    context = {'news_list': news_list}
    return render(request, 'news.html', context)
