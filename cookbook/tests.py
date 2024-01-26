from django.test import TestCase
from django.urls import reverse
from django import setup

from .models import Author, Recipe
from os import environ
from uuid6 import uuid7

environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
setup()


class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.author = Author.objects.create(
            first_name="John", last_name="Doe", misc_info="Test Author"
        )

    def test_author_creation(self):
        self.assertTrue(isinstance(self.author, Author))

    def test_string_representation(self):
        self.assertEqual(str(self.author), "John Doe")

    def test_slug_field_auto_generation(self):
        self.assertEqual(self.author.slug, "john-doe")

    def test_get_absolute_url(self):
        self.assertEqual(
            self.author.get_absolute_url(),
            reverse("cookbook:author-detail", kwargs={"slug": self.author.slug}),
        )


class RecipeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        from .models import Author, Recipe

        cls.author = Author.objects.create(
            first_name="John", last_name="Doe", misc_info="Test Author"
        )
        cls.recipe = Recipe.objects.create(
            author=cls.author,
            title="Test Recipe",
            category="Test Category",
            ingredients="Ingredient 1\nIngredient 2",
            instructions="Step 1\nStep 2",
            misc_info="Test Recipe Info",
        )

    def test_recipe_creation(self):
        self.assertTrue(isinstance(self.recipe, Recipe))
        self.assertEqual(self.recipe.author, self.author)

    def test_string_representation(self):
        self.assertEqual(str(self.recipe), "Test Recipe by John Doe")

    def test_slug_field_auto_generation(self):
        self.assertEqual(self.recipe.slug, "test-recipe")

    def test_get_absolute_url(self):
        self.assertEqual(
            self.recipe.get_absolute_url(),
            reverse("cookbook:recipe-detail", kwargs={"slug": self.recipe.slug}),
        )

    def test_ingredients_as_list(self):
        self.assertEqual(
            self.recipe.ingredients_as_list(), ["Ingredient 1", "Ingredient 2"]
        )

    def test_instructions_as_list(self):
        self.assertEqual(self.recipe.instructions_as_list(), ["Step 1", "Step 2"])
