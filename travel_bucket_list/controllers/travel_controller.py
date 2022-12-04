from flask import Blueprint, render_template, request, redirect
import repositories.user_repository as user_repository
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

destination_blueprint = Blueprint("destinations", __name__)

@destination_blueprint.route("/home")
def home(): 
    return render_template("index.html")

@destination_blueprint.route("/country/<country_id>")
def country(country_id):
    country_repository.select(country_id)
    return render_template("visited_country/visited_country.html", country = country)

