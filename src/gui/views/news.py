from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..models import News


@login_required
def show_news(request):
    news_list = News.objects.all()
    context = {'news_list': news_list}
    return render(request, 'news.html', context)
