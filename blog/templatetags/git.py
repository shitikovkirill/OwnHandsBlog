from django import template
from github import Github

register = template.Library()

@register.simple_tag
def get_user(user_name):
    git = Github()
    user = git.get_user(user_name)
    return user

