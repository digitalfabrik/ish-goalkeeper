"""
Template tags in relation to groups
"""
from django import template

register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_name):
    """
    Test if a user is member of a group
    """
    return user.groups.filter(name=group_name).exists()
