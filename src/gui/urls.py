from django.urls import path
from django.http import HttpResponseRedirect
from . import views

urlpatterns = [
    path('', lambda r: HttpResponseRedirect('login/')),
    path('login/', views.login_user, name='login_user')
]
