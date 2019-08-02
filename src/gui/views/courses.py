"""
View for courses of users.
"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from ..models import CourseUser, Course, CourseLesson, Lesson


@login_required
def show_courses(request):
    """
    Get courses for user
    """
    # pylint: disable=E1101
    courses_user = CourseUser.objects.filter(user=request.user)
    courses = Course.objects.filter(id__in=courses_user, active=True)
    context = {'course_list': courses}
    return render(request, 'courses.html', context)


@login_required
def course_details(request, course_id=None):
    """
    Details about a course
    """
    context = {}
    # pylint: disable=E1101
    course_detail = Course.objects.get(id=course_id)
    lesson_list = (CourseLesson.objects.filter(course=course_id)
                   .values_list('lesson', flat=True))
    if len(lesson_list) == 1:
        lesson_list = Lesson.objects.get(id=lesson_list[0]).get_children()
    else:
        lesson_list = Lesson.objects.filter(id__in=lesson_list)
    course_user_list = (CourseUser.objects.filter(course=course_id)
                        .values_list('user', flat=True))
    user_list = User.objects.filter(id__in=course_user_list)
    context = {'course': course_detail,
               'lesson_list': lesson_list,
               'user_list': user_list,
               'back_link': "/gui/courses/"}
    return render(request, 'course.html', context)


@login_required
def course_lesson(request, course_id=None, lesson_id=None):
    """
    Display a lesson
    """
    course_id = course_id
    lesson_id = lesson_id
    # pylint: disable=E1101
    course_detail = Course.objects.get(id=course_id)
    lesson = Lesson.objects.get(id=lesson_id)
    sub_lesson_list = lesson.get_children()
    if lesson.is_root_node():
        parent_link = "/gui/course/{}/".format(course_id)
    else:
        parent = lesson.get_ancestors(ascending=True, include_self=False)[0]
        parent_link = "/gui/course/{}/{}/".format(course_id, parent.id)
    if lesson.needs_feedback(course_id):
        print("needs_feedback")
    context = {'lesson_details': lesson,
               'sub_lesson_list': sub_lesson_list,
               'course': course_detail,
               'back_link': parent_link}
    return render(request, 'lesson.html', context)
