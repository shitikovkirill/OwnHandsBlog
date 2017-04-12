from django import template
from blog.models import SettingsModel
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()


def get_option(value):
    """Get value from site settings"""
    try:
        return SettingsModel.objects.get(option=value)
    except ObjectDoesNotExist:
        return ''

register.filter('get_option', get_option)
