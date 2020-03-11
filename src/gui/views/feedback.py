"""
Module handling feedback for lessons
"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from django.core.mail import EmailMessage
from django.conf import settings
from ..models import Lesson, Feedback, Course, access_course


@csrf_protect
@access_course
@login_required
def feedback_form(request, course_id=None, lesson_id=None):
    """
    Feedback form for lessons
    """
    # pylint: disable=E1101
    lesson = Lesson.objects.get(id=lesson_id)
    if not lesson.feedback_required:
        return HttpResponseRedirect('/gui/course/{}/{}/'.format(
            course_id, lesson_id))
    course = Course.objects.get(id=course_id)
    try:
        feedback = Feedback.objects.get(course=course, lesson=lesson)
    except Feedback.DoesNotExist:
        feedback = Feedback(course=course,
                            lesson=lesson)
        feedback.save()
    if 'save' in request.POST:
        feedback.male = request.POST['male']
        feedback.female = request.POST['female']
        feedback.other = request.POST['other']
        feedback.positive = request.POST['positive']
        feedback.negative = request.POST['negative']
        feedback.comment = request.POST['comment']
        feedback.childprotection = request.POST['childprotection']
        feedback.save()
        saved = True

        email = EmailMessage('ISH Goalkeeper - Neues Feedback',
                             "Neues oder geändertes Feedback unter "
                             "https://{}/admin/gui/feedback/{}/".format(
                                 request.get_host(),
                                 feedback.id),
                             reply_to=[request.user.email],
                             from_email=settings.EMAIL_HOST_USER,
                             to=[settings.EMAIL_CONTACT])
        email.send()

    else:
        saved = False

    context = {'lesson': lesson,
               'feedback': feedback,
               'saved': saved,
               'back_link': '/gui/course/{}/{}/'.format(course_id,
                                                        lesson_id)}
    course = course
    feedback = feedback
    return render(request, 'feedback.html', context)
