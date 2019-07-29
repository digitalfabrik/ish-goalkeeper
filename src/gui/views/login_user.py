from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def login_screen(request):
    template = loader.get_template('login.html')
    context = {
        'latest_question_list': [],
    }
    return HttpResponse(template.render(context, request))

@csrf_protect
def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect("/gui/news")
    return HttpResponseRedirect("/gui/")

