import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_recetas")
def get_recetas():
    recetas = list(mongo.db.recetas.find())
    return render_template("recipes.html", recetas=recetas, page_title="Recipes")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.UserId.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        } 
        mongo.db.UserId.insert_one(register)

        #put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Succesfull")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        #check if username exists in db
        existing_user = mongo.db.UserId.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exists
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.UserId.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:    
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_recipe", methods=["GET", "POST"]) 
def add_recipe():
    # add new recipe to db
    if request.method == "POST":
        receta = {
            "foodType_name": request.form.get("foodType_name"),
            "receta_name": request.form.get("receta_name"),
            "cooking_instructions": request.form.get("cooking_instructions"),
            "created_by": session["user"]
        }
        mongo.db.recetas.insert_one(receta)
        flash("Recipe Succesfully Added")
        return redirect(url_for("get_recetas"))

    foodTypes = mongo.db.foodTypes.find().sort("foodType_name", 1) 
    return render_template("add_recipe.html", foodTypes=foodTypes) 


@app.route("/edit_recipe/<receta_id>", methods=["GET", "POST"])
def edit_recipe(receta_id):
    # edit recipe on db
    if request.method == "POST":
        submit = {
            "foodType_name": request.form.get("foodType_name"),
            "receta_name": request.form.get("receta_name"),
            "cooking_instructions": request.form.get("cooking_instructions"),
            "created_by": session["user"]
        }
        mongo.db.recetas.update({"_id": ObjectId(receta_id)}, submit)
        flash("Recipe Succesfully Updated")
        
    receta = mongo.db.recetas.find_one({"_id": ObjectId(receta_id)})
    foodTypes = mongo.db.foodTypes.find().sort("foodType_name", 1) 
    return render_template("edit_recipe.html", receta=receta, foodTypes=foodTypes) 


@app.route("/delete_recipe/<receta_id>")
def delete_recipe(receta_id):
    mongo.db.recetas.remove({"_id": ObjectId(receta_id)})
    flash("Recipe Succesfully Deleted")
    return redirect(url_for("get_recetas"))


@app.route("/get_foodtypes")
def get_foodtypes():
    foodtypes = list(mongo.db.foodTypes.find().sort("foodType_name", 1))
    return render_template("foodtypes.html", foodtypes=foodtypes)


@app.route("/add_foodtype", methods=["GET", "POST"])
def add_foodtype():
    if request.method == "POST":
        foodtype = {
            "foodType_name": request.form.get("foodType_name")
        }
        mongo.db.foodTypes.insert_one(foodtype)
        flash("New Food Type added")
        return redirect(url_for("get_foodtypes"))

    return render_template("add_foodtype.html")


@app.route("/edit_foodtype/<foodtype_id>", methods=["GET", "POST"] )
def edit_foodtype(foodtype_id):
    if request.method == "POST":
        submit = {
            "foodType_name": request.form.get("foodType_name") 
        }
        mongo.db.foodTypes.update({"_id": ObjectId(foodtype_id)}, submit)
        flash("Food Type Succesfully Updated")
        return redirect(url_for("get_foodtypes"))

    foodtype = mongo.db.foodTypes.find_one({"_id": ObjectId(foodtype_id)})
    return render_template("edit_foodtype.html", foodtype=foodtype)


@app.route("/delete_foodtype/<foodtype_id>")
def delete_foodtype(foodtype_id):
    mongo.db.foodTypes.remove({"_id": ObjectId(foodtype_id)})
    flash("Food Type Succesfully Deleted")
    return redirect(url_for("get_foodtypes"))


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)