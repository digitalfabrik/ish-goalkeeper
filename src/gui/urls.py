"""
URL routing
"""
from django.urls import path
from . import views

# pylint: disable=C0103
urlpatterns = [
    path('', views.login_screen, name="login_screen"),
    path('login/', views.login_user, name='login_user'),
    path('news/', views.show_news, name="news"),
    path('logout/', views.logout_user, name="logout_user"),
    path('privacy/', views.privacy_statement, name="privacy_statement"),
    path('contact/', views.contact_form, name="contact_form"),
    path('send_contact/', views.send_contact_form, name="send_contact_form"),
    path('profile/', views.edit_profile, name="edit_profile"),
    path('courses/', views.show_courses, name="show_courses"),
    path('course/<int:course_id>/',
         views.course_details,
         name="course_details"),
    path('course/<int:course_id>/<int:lesson_id>/',
         views.course_lesson,
         name="course_lesson"),
]
