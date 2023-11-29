# this  code to parses the recipe_df.json file and add the authors to the database
# only works if the authors have been cleaned up and are in the format "first_name last_name"

import json
from cookbook.models import Author, Recipe


json_file_path = "/home/jake2237/Github_repos/mywebsite/recipe_df.json"

author_objects = Author.objects.all()
recipe_dicts = []

with open(json_file_path) as f:
    data = json.load(f)
    for recipe in data:
        author = recipe["author"].split(" ")
        recipe_dict = {
            "author": author_objects.get(first_name=author[0], last_name=author[1]),
            "title": recipe["title"],
            "category": recipe["category"],
            "ingredients": recipe["ingredients"],
            "instructions": recipe["instructions"],
        }
        recipe_dicts.append(recipe_dict)


for obj in recipe_dicts:
    m = Recipe(**obj)
    m.save()
