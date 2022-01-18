from urllib import response
from SearchRecipes_Flask import main_functions
import requests
from flask_wtf import FlaskForm
from wtforms import StringField

class SearchForRecipes (FlaskForm):
    meal = StringField('Meal')
    include = StringField('Include')
    exclude = StringField('Exclude')

def get_data(meal, include, exclude):
    api_key_dict = main_functions.read_from_file('SearchRecipes_Flask/JSON_Files/api_key.json')
    api_key = api_key_dict["api_key"]

    url = "https://api.spoonacular.com/food/videos/search?query=" \
          + meal + "&excludeIngredients=" + exclude + "&includeIngredients="\
          + include + "&apiKey=" + api_key
    
    # 1 - Make the api request using the requests .get method
    print("1) Making API request: ")
    response = requests.get(url).json()
    print("Done")

    # 2 - Save the response as a json file on the specified directory
    print("2) Saving JSON Info received from API request")
    main_functions.save_to_file(response, "SearchRecipes_Flask/JSON_Files/recipes.json")
    print("Done")

    # 3 - Read the JSON file and save it to the specified variable
    print("3) Reading information from JSON File")
    recipes = main_functions.read_from_file("SearchRecipes_Flask/JSON_Files/recipes.json")
    print("Done")

    # 4 - Return found recipes
    return recipes