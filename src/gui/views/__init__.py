from .login_user import login_user, login_screen, logout_user
from .news import show_news
from .privacy import privacy_statement
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("ISH end user gui.")
