"""
Takes care of logging user in.
"""
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def login_screen(request):
    """
    Default login screen. Redirect if user is already
    logged in.
    """
    template = loader.get_template('login.html')
    context = {
        'latest_question_list': [],
    }
    if request.user.is_authenticated:
        return HttpResponseRedirect("/gui/news")
    return HttpResponse(template.render(context, request))


@csrf_protect
def login_user(request):
    """
    Verify user credentials.
    """
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect("/gui/news")
    return HttpResponseRedirect("/gui/")


def logout_user(request):
    """
    Log user outi
    """
    logout(request)
    return HttpResponseRedirect("/gui/")
