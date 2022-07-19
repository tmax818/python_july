from flask_app import app, render_template, redirect, request, bcrypt, session,flash
from flask_app.models.recipe import Recipe


@app.route('/recipes')
def recipes():
    return render_template('recipes.html')

@app.route('/recipes/new')
def new_recipe():
    return render_template('new_recipe.html')

@app.route('/create/recipe', methods=['post'])
def create_recipe():
    print(request.form)
    Recipe.save(request.form)
    return redirect('/recipes')