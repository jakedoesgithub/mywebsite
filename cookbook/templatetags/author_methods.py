from cookbook.models import Author

from django import template

register = template.Library()


@register.simple_tag
def get_author_list_alphabetical():
    """Returns a list of all authors in alphabetical order."""
    return Author.objects.order_by("last_name", "first_name")
