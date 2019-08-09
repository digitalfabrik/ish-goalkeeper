"""
Provides needed information for all templates,
usually user name, location, etc for menu.
"""
from .models import Profile, CourseUser
from .models import Logo


def profile_processor(request):
    """
    Get user information for menu.
    """
    # pylint: disable=E1101
    try:
        logo = Logo.objects.get(main=True).logo.url
    except Logo.DoesNotExist:
        logo = ""
    if not request.user.is_authenticated:
        return {'user_info': {'location': '', 'name': '', 'courses': ''},
                'main_logo': logo}
    user_info = {}
    # pylint: disable=E1101
    profile = Profile.objects.filter(user=request.user)
    if not profile:
        user_info['location'] = "unbekannt"
    else:
        user_info['location'] = profile[0].location
    if request.user.first_name:
        user_info['name'] = request.user.first_name
    else:
        user_info['name'] = request.user
    courses = CourseUser.objects.filter(user=request.user)
    user_info['courses'] = len(courses)

    return {'user_info': user_info, 'main_logo': logo}
