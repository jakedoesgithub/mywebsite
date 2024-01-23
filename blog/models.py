from django.db import models
from django.urls import reverse
from django.utils.encoding import iri_to_uri
from django.utils.text import slugify

from django_extensions.db.fields import AutoSlugField
from uuid6 import uuid7


class Tag(models.Model):
    """Model definition for Tag
    Note: to get the queryset you can use the following:
    queryset = Tag.objects.filter(post__post_id__isnull=False).distinct()"""

    tag_id = models.UUIDField(
        primary_key=True, default=uuid7, editable=False, unique=True
    )
    name = models.CharField(max_length=50, help_text="Tag name")
    slug = AutoSlugField(populate_from=["name"], editable=False, unique=True)

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

    def __str__(self):
        """Unicode representation of Tag."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a particular Tag instance."""
        return reverse("blog:tag-detail", kwargs={"slug": self.slug})


class Post(models.Model):
    post_id = models.UUIDField(
        primary_key=True, default=uuid7, editable=False, unique=True
    )
    title = models.CharField(max_length=255, help_text="Blog post title")
    date_posted = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, help_text="Tags for the blog post")
    body = models.TextField(help_text="Post body")
    snippet = models.TextField(help_text="Post snippet", default=body.split("\n\n")[0])

    slug = AutoSlugField(populate_from=["title"], editable=False, unique=True)

    class Meta:
        """Meta definition for Post."""

        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        """Unicode representation of Post."""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a particular Post instance."""
        return reverse("blog:post-detail", kwargs={"slug": self.slug})
