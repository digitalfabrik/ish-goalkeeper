from django.http import HttpResponse
from django.template import loader


def login_user(request):
    template = loader.get_template('login.html')
    context = {
        'latest_question_list': [],
    }
    return HttpResponse(template.render(context, request))
