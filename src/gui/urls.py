from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_screen, name="login_screen"),
    path('login/', views.login_user, name='login_user'),
    path('news/', views.show_news, name="news"),
    path('logout/', views.logout_user, name="logout_user"),
    path('privacy/', views.privacy_statement, name="privacy_statement"),
]
