"""
View for courses of users.
"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from ..models import CourseUser, Course, access_course
from .lessons import get_lessons, get_root_lesson_ids


@login_required
def show_courses(request):
    """
    Get courses for user
    """
    # pylint: disable=E1101
    courses_user = (CourseUser.objects.filter(user=request.user)
                    .values_list('user', flat=True))
    courses = Course.objects.filter(id__in=courses_user, active=True)
    context = {'course_list': courses}
    return render(request, 'courses.html', context)


@access_course
@login_required
def course_details(request, course_id=None):
    """
    Details about a course
    """
    context = {}
    # pylint: disable=E1101
    course_detail = Course.objects.get(id=course_id)
    course_user_list = (CourseUser.objects.filter(course=course_id)
                        .values_list('user', flat=True))
    user_list = User.objects.filter(id__in=course_user_list)
    lesson_list = get_lessons(course_id)
    context = {'course': course_detail,
               'lesson_list': lesson_list,
               'user_list': user_list,
               'back_link': "/gui/courses/"}
    return render(request, 'course.html', context)


def get_parent_link(lesson, course_id):
    """
    Get link to next higher level. If a course has only
    on lesson directly linked, skip this single lesson.
    """
    if lesson.is_root_node():
        parent_link = "/gui/course/{}/".format(course_id)
    else:
        parent = lesson.get_ancestors(ascending=True, include_self=False)[0]
        root_ids = get_root_lesson_ids(course_id)
        if lesson.id in root_ids:
            parent_link = "/gui/course/{}/".format(course_id)
        else:
            parent_link = "/gui/course/{}/{}/".format(course_id, parent.id)
    return parent_link
