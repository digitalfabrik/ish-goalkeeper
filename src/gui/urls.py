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
    path('profile/', views.edit_profile, name="edit_profile"),
    path('courses/', views.show_courses, name="show_courses"),
    path('timesheet/', views.timesheet, name="timesheet"),
    path('course/<int:course_id>/',
         views.course_details,
         name="course_details"),
    path('course/<int:course_id>/<int:lesson_id>/',
         views.lesson_details,
         name="lesson_details"),
    path('feedback/<int:course_id>/<int:lesson_id>/',
         views.feedback_form,
         name="feedback_form"),
    path('statistics/<int:course_id>/',
         views.statistics,
         name="statistics"),
    path('mnews/<int:news_id>',
         views.show_news, name='mnews'),
    path('knowledge/',
         views.knowledge_article, name='knowledge'
        ),
    path('knowledge/<int:knowledge_article_id>',
         views.knowledge_article, name='knowledge'
        ),
]
