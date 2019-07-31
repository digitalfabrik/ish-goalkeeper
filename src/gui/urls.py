from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_screen, name="login_screen"),
    path('login/', views.login_user, name='login_user'),
    path('news/', views.show_news, name="news"),
    path('logout/', views.logout_user, name="logout_user"),
    path('privacy/', views.privacy_statement, name="privacy_statement"),
    path('contact/', views.contact_form, name="contact_form"),
    path('send_contact/', views.send_contact_form, name="send_contact_form"),
    path('profile/', views.edit_profile, name="edit_profile"),
]
