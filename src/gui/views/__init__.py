from .login_user import login_user, login_screen, logout_user
from .news import show_news
from .privacy import privacy_statement
from .contact import contact_form, send_contact_form
from .profile import edit_profile
from .courses import show_courses, course_details, course_lesson
from django.shortcuts import render
from django.http import HttpResponse

