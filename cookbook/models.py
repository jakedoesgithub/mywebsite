from django.db import models
from django.utils.encoding import iri_to_uri
from django.utils.text import slugify
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from uuid6 import uuid7


class Author(models.Model):
    """Model definition for a recipe Author."""

    author_id = models.UUIDField(
        primary_key=True, default=uuid7, editable=False, unique=True
    )
    first_name = models.CharField(
        blank=False,
        max_length=50,
        help_text="Author's first name",
    )
    last_name = models.CharField(
        blank=False, max_length=50, help_text="Author's last name"
    )
    misc_info = models.TextField(
        max_length=500, help_text="Miscellaneous information about the author"
    )
    slug = AutoSlugField(populate_from=["first_name", "last_name"], editable=False)

    class Meta:
        """Meta definition for Author."""

        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        """Unicode representation of Author."""
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        """Returns the url to access a particular Author instance."""
        return reverse("cookbook:author-detail", kwargs={"slug": self.slug})


class Recipe(models.Model):
    """Model definition for Recipe."""

    recipe_id = models.UUIDField(
        primary_key=True, default=uuid7, editable=False, unique=True
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        help_text="Author of the recipe",
    )
    title = models.CharField(
        max_length=70, help_text="Recipe name", blank=False, unique=True
    )
    category = models.CharField(
        max_length=50, help_text="Recipe category", default="Uncategorized"
    )
    ingredients = models.TextField(
        max_length=2000, help_text="Ingredients required for the recipe"
    )
    instructions = models.TextField(
        max_length=2000, help_text="Cooking instructions for the recipe"
    )
    misc_info = models.TextField(
        max_length=500, help_text="Miscellaneous information about the recipe"
    )
    slug = AutoSlugField(populate_from=["title"], editable=False, unique=True)

    class Meta:
        verbose_name = "Recipe"
        verbose_name_plural = "Recipes"

    def __str__(self):
        """Unicode representation of Recipe."""
        return f"{self.title} by {self.author}"

    def get_absolute_url(self):
        """Returns the url to access a particular Recipe instance."""
        return reverse("cookbook:recipe-detail", kwargs={"slug": self.slug})
