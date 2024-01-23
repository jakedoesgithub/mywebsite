from cookbook.models import Recipe

from django import template

register = template.Library()


@register.simple_tag
def get_recipe_categories():
    """
    Returns a list of all the recipe categories.
    Make sure to use {% load recipe_methods %} at the top of the template.
    """
    return [
        "Cajun Favorites",
        "Meats",
        "Seafood",
        "Bread",
        "Pie",
        "Cake",
        "Candy and Other Desserts",
        "Misc",
    ]
