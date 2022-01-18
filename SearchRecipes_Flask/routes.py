from SearchRecipes_Flask import app, forms
from flask import request, render_template

@app.route('/')
@app.route('/search',methods=["GET","POST"])
def search():
    search_form = forms.SearchForRecipes(request.form)

    if request.method == 'POST':
        # Assign to the following variables the input values by the user
        meal = request.form['meal']
        include = request.form['include']
        exclude = request.form['exclude']

        # Pass variables as arguments to the get_date function
        # Assign the return value to recipes
        recipes = forms.get_data(meal, include, exclude)

        # Accessing the list available in the json:
        print("Before")
        print(recipes)
        recipes = recipes["videos"]
        print("After")
        print(recipes)

        return render_template('recipes_results.html', form=search_form, meal=meal, include=include,
                                exclude=exclude, recipes=recipes)
    return render_template('recipes_search.html', form=search_form)