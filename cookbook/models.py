from django.db import models
from django.utils.encoding import iri_to_uri
from django.utils.text import slugify
from django.urls import reverse
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
    slug = models.SlugField(
        editable=False,
        default=slugify(f"{first_name} {last_name}"),
    )

    class Meta:
        """Meta definition for Author."""

        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        """Unicode representation of Author."""
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        """Returns the url to access a particular Author instance."""
        return reverse("author-detail", kwargs={"slug": self.slug})


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
    name = models.CharField(
        max_length=70, help_text="Recipe name", blank=False, unique=True
    )
    misc_info = models.TextField(
        max_length=500, help_text="Miscellaneous information about the recipe"
    )
    slug = models.SlugField(
        editable=False,
        default=slugify(name),
        max_length=80,
    )

    class Meta:
        verbose_name = "recipe"
        verbose_name_plural = "recipes"

    def __str__(self):
        """Unicode representation of Recipe."""
        return f"{self.name}"

    def get_absolute_url(self):
        """Returns the url to access a particular Recipe instance."""
        return reverse("recipe-detail", kwargs={"slug": self.slug})
