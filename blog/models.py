from django.db import models
from django.urls import reverse
from django.utils.encoding import iri_to_uri
from django.utils.text import slugify
from django.contrib.postgres.fields import ArrayField
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
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

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
    tags = models.ManyToManyField(
        Tag, related_name="posts", help_text="Tags for the blog post"
    )
    content = models.TextField(help_text="Post content")
    description = models.TextField(
        help_text="Post description", default="No description for this post"
    )
    slug = AutoSlugField(populate_from=["title"], editable=False, unique=True)

    class Meta:
        """Meta definition for Post."""

        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ["-date_posted"]

    def __str__(self):
        """Unicode representation of Post."""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a particular Post instance."""
        return reverse("blog:post-detail", kwargs={"slug": self.slug})
