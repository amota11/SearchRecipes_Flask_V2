SearchRecipes_Flask_V2 
Originally written for my Component-Based Software Developemnt (COP 4814) under the guidance of Prof. Greg Reis. [FIU - Fall 2020]. 

Project focused writing a simple web application with the following functionlaty:
    1) Request data from a public API
    2) Consume said data and create a JSON file 
    3) Displayed desired info to the user in formatted HTML page.

We were allowed to choose a public API of our liking, so I took this opportunity to integrate my passion for cooking into the project by using the Spoonacular API
to search for recipes with a simple criteria:
    1) Recipe name
    2) Include ingredient
    3) Exclude ingredient
    
 Front-end is composed of two barebones HTML pages:
    1) Search page with three input fields matching the criteria above.
    2) Results page with a table for found recipes and a link for new search.
    
 Back-end is written in Python, using the Flask micro web framework and the following libraries: requests, Flask-WTF, and wtf-forms.
