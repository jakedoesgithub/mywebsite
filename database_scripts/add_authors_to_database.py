# this  code to parses the recipe_df.json file and add the authors to the database
# only works if the authors have been cleaned up and are in the format "first_name last_name"

import json
from cookbook.models import Author


json_file_path = "/home/jake2237/Github_repos/mywebsite/recipe_df.json"

authors = []

with open(json_file_path) as f:
    data = json.load(f)
    for recipe in data:
        author_name = recipe["author"].split(" ")
        author_dict = {
            "first_name": author_name[0],
            "last_name": author_name[1],
            "misc_info": "",
        }
        if author_dict not in authors:
            authors.append(author_dict)


for obj in authors:
    m = Author(**obj)
    m.save()
