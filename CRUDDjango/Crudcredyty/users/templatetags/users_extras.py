from django import template
from users.models import User

register = template.Library()

@register.simple_tag
def get_user_list():
    users = User.objects.all()
    return users