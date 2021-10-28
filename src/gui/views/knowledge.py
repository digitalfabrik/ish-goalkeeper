"""
Views for knowledge articles
"""
from django.shortcuts import render  # pylint: disable=E0401
from django.contrib.auth.decorators import login_required  # pylint: disable=E0401
from ..models import KnowledgeArticle  # pylint: disable=E0401


@login_required
def knowledge_article(request, knowledge_article_id=None):
    """
    Display a knowledge article and its children. If no ID is provided, list all root node articles.
    """
    # pylint: disable=E1101
    if knowledge_article_id is None:
        children = KnowledgeArticle.objects.filter(level=0).order_by("title")
        article = None
    else:
        children = KnowledgeArticle.objects.filter(parent=knowledge_article_id).order_by("title")
        article = KnowledgeArticle.objects.get(id=knowledge_article_id)
    context = {'article': article,
               'children': children,
              }
    return render(request, 'knowledge.html', context)
