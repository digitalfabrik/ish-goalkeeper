"""
Views for single lessons
"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..models import Course, CourseLesson, Lesson, Feedback
from ..models import LessonMetaData, Attachment


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


def needs_feedback(lesson, course_id):
    """
    Does this lesson or any of its descendants need
    feedback?
    0 = no feedback required
    1 = feedback not yet provided
    2 = feedback provided
    """
    descendants = lesson.get_descendants(include_self=True)
    for descendant in descendants:
        if descendant.feedback_required:
            # If feedback is needed, check if already provided
            try:
                # pylint: disable=E1101
                feedback = Feedback.objects.get(lesson_id=descendant.id,
                                                course_id=course_id)
            except Feedback.DoesNotExist:
                # feedback is required but not yet provided
                return 1
            else:
                if feedback.negative == 0 and feedback.positive == 0:
                    # Object has been created but no data provided
                    return 1
                # Feedback has been provided
                return 2
    return 0


def get_root_lesson_ids(course_id):
    """
    Get plain list of root lessons for user. If there is only
    one root node, its children will be returned directly.
    """
    # pylint: disable=E1101
    lesson_id_list = (CourseLesson.objects.filter(course=course_id)
                      .values_list('lesson', flat=True))
    if (len(lesson_id_list) == 1 and Lesson.objects
            .get(id=lesson_id_list[0])
            .get_children()):
        # if a course has only one lesson, but this lesson has
        # children, then show them directly
        lesson_id_list = (Lesson.objects.get(id=lesson_id_list[0])
                          .get_children().values_list('id', flat=True))
    return lesson_id_list


def get_lesson_meta(lesson_id):
    """
    Get meta information about a lesson
    """
    # pylint: disable=E1101
    lesson_meta_list = (LessonMetaData.objects.filter(lesson=lesson_id)
                        .prefetch_related())
    result = []
    for item in lesson_meta_list:
        result.append({
            'description': item.description.description,
            'value': item.value,
            'icon': item.description.icon})
    return result


def get_lesson_attachments(lesson_id):
    """
    Get attachments for a lesson
    """
    # pylint: disable=E1101
    lesson_attachments = Attachment.objects.filter(lesson=lesson_id)
    result = []
    for attachment in lesson_attachments:
        url = attachment.attached_file.url
        result.append({'description': attachment.description,
                       'url': url,
                       'is_image': (
                           True if url.lower().endswith(".jpg")
                           or url.lower().endswith(".png")
                           or url.lower().endswith(".jpeg")
                           else False),
                       'attached_file': attachment.attached_file, })
    return result


def get_lessons(course_id, lesson=None):
    """
    Get list of lessons. If lesson_id is provided,
    then sublessons will be returned.
    """
    lesson_list = []
    if lesson is None:
        lesson_list = Lesson.objects.filter(
            id__in=get_root_lesson_ids(course_id))
    else:
        lesson_list = lesson.get_children()
    result = []
    for lesson_item in lesson_list:
        result.append({
            'id': lesson_item.id,
            'title': lesson_item.title,
            'needs_feedback': needs_feedback(lesson_item, course_id),
            'mandatory': lesson_item.mandatory,
        })
    return result


@login_required
def lesson_details(request, course_id=None, lesson_id=None):
    """
    Display a lesson
    """
    course_id = course_id
    lesson_id = lesson_id
    # pylint: disable=E1101
    course_detail = Course.objects.get(id=course_id)
    lesson = Lesson.objects.get(id=lesson_id)
    context = {'lesson_details': lesson,
               'sub_lesson_list': get_lessons(course_id, lesson),
               'course': course_detail,
               'back_link': get_parent_link(lesson, course_id),
               'lesson_meta': get_lesson_meta(lesson_id),
               'lesson_attachments': get_lesson_attachments(lesson_id)}
    return render(request, 'lesson.html', context)
