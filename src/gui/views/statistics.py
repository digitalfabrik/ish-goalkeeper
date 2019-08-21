"""
Module showing feedback statistics
"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..models import Feedback, Course, access_course


def generate_pie_chart(pos, neg):
    """
    Render image and return it in a base64 encoded string
    """
    import matplotlib.pyplot as plt
    import base64
    from io import BytesIO

    labels = ["Positiv", "Negativ"]
    counts = [pos, neg]
    explode = (0, 0)
    plt.rcParams.update({'font.size': 16})
    fig1, ax1 = plt.subplots()
    ax1.pie(counts, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figdata_png = base64.b64encode(figfile.getvalue())
    return figdata_png.decode('utf8')


@login_required
@access_course
def statistics(request, course_id=None):
    """
    Feedback form for lessons
    """
    # pylint: disable=E1101
    course = Course.objects.get(id=course_id)
    feedback = Feedback.objects.filter(course=course)
    sum_pos = 0
    sum_neg = 0
    for item in feedback:
        sum_pos = item.positive + sum_pos
        sum_neg = item.negative + sum_neg
    context = {'course': course,
               'pie': generate_pie_chart(sum_pos, sum_neg),
               'back_link': '/gui/course/{}'.format(course_id),
               'positive': sum_pos,
               'negative': sum_neg}
    return render(request, 'statistics.html', context)
