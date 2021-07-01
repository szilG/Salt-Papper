import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
if os.path.exists("env.py"):
    import env

# Instance of Flask
app = Flask(__name__)

# MongoDB Configuration
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

# MongoDB Global Variable
mongo = PyMongo(app)


@app.route("/")
@app.route("/home/")
def home():
    """To display all recipes by posted date"""
    recipes = list(mongo.db.recipes.find().sort("_id", -1))
    
    return render_template(
        "home.html",
        recipes=recipes,)


@app.route("/recipes/<categories>")
def recipes(categories):
    """To display recipes of that specific category by posted date"""
    if categories == "all":
        recipes = list(mongo.db.recipes.find().sort("_id", -1))
    elif categories == "mains":
        recipes = list(mongo.db.recipes.find({"category_name": "Mains"}))
    elif categories == "breakfast":
        recipes = list(mongo.db.recipes.find({"category_name": "Breakfast"}))
    elif categories == "desserts":
        recipes = list(mongo.db.recipes.find({"category_name": "Desserts"}))
    elif categories == "starters":
        recipes = list(mongo.db.recipes.find({"category_name": "Starters"}))
    elif categories == "drinks":
        recipes = list(mongo.db.recipes.find({"category_name": "Drinks"}))
    else:
        recipes = list(mongo.db.recipes.find().sort("_id", -1))

    return render_template(
        "recipes.html", recipes=recipes, categories=categories)


@app.route("/search/", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("home.html", recipes=recipes)


@app.route("/register/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("home"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("home.html")


@app.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            # make variable to password check
            does_password_match = check_password_hash(
                existing_user["password"],
                request.form.get("password")
            )
            if does_password_match:
                session["user"] = request.form.get("username").lower()
                return redirect(url_for("profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password. Please try Again")
                return redirect(url_for("home"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password Please try Again")
            return redirect(url_for("home"))

    return render_template("home.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    if not session.get("user"):
        return render_template("error_handlers/404.html")

    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        if session["user"] == "admin222":
            user_recipes = list(mongo.db.recipes.find())
        else:
            user_recipes = list(
                mongo.db.recipes.find({"username": session["user"]}))
        return render_template(
            "profile.html", username=username, user_recipes=user_recipes)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    session.pop("user")
    return redirect(url_for("home"))


# Add New Recipe To DB
@app.route("/add_recipe/", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        """
        Create dictionary
        """
        recipe = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "chef": request.form.get("chef"),
            "serves": request.form.get("serves"),
            "difficulty_level": request.form.get("difficulty_level"),
            "prep_time": request.form.get("prep_time"),
            "cook_time": request.form.get("cook_time"),
            "image": request.form.get("image"),
            "ingredients": request.form.get("ingredients"),
            "method": request.form.get("method"),
            "description": request.form.get("description"),
            "username": session["user"],
            "formated_date": datetime.today().strftime("%d-%m-%Y")
        }
        """
        Insert form to database
        """
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe is successfully added")
        return redirect(url_for("profile", username=session['user']))

    categories = mongo.db.categories.find().sort("category_name", 1)
    difficulties = mongo.db.difficulty.find().sort("difficulty_level", 1)
    return render_template(
        "add_recipe.html", categories=categories, difficulties=difficulties)


# Edit recipe
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        """
        Create dictionary
        """
        submit = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "chef": request.form.get("chef"),
            "serves": request.form.get("serves"),
            "difficulty_level": request.form.get("difficulty_level"),
            "prep_time": request.form.get("prep_time"),
            "cook_time": request.form.get("cook_time"),
            "image": request.form.get("image"),
            "ingredients": request.form.get("ingredients"),
            "method": request.form.get("method"),
            "description": request.form.get("description"),
            "username": session["user"],
            "formated_date": datetime.today().strftime("%d-%m-%Y")
        }
        """
        Insert form to database
        """
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe is successfully updated")
        return redirect(url_for("profile", username=session['user']))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    difficulties = mongo.db.difficulty.find().sort("difficulty_level", 1)
    return render_template(
        "edit_recipe.html",
        recipe=recipe, categories=categories, difficulties=difficulties)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe successfully deleted")
    return redirect(url_for("profile", username=session['user']))


@app.route("/get_categories/")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template(
        "categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New category Added")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Category Successfully Updated")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template(
        "edit_category.html", category=category)


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("get_categories"))


# Single Recipe route
@app.route("/single_recipe/<recipe_id>")
def single_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("single_recipe.html", recipe=recipe)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
