import requests
import json

# get recipe from edamam api
def get_recipe(ingredients):
    # api
    app_id = 'da35d90f'
    app_key = '7fc86bc9688108fcd0ab1cce57884a7a'

    # url
    url = 'https://api.edamam.com/search?q=' + ingredients + '&app_id=' + app_id + '&app_key=' + app_key

    # get response
    response = requests.get(url)

    # get json
    data = response.json()

    # get recipes
    recipes = data['hits']

    # print recipes in json format
    print(json.dumps(recipes, indent=4))

    return recipes

get_recipe('basil')