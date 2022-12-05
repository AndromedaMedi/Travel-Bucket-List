from flask import Blueprint, render_template, request, redirect
import repositories.user_repository as user_repository
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository
from models.user import User
from models.country import Country
from models.city import City

destination_blueprint = Blueprint("destinations", __name__)

# IDEX
# GET '/'
# Show the home page with the data needing to be displayed
@destination_blueprint.route("/")
def home():
    user= user_repository.select_all()[0]
    countries_visited = country_repository.select_all_visited()
    countries_to_visit = country_repository.select_all_to_visit()
    cities_to_visit = city_repository.select_all_to_visit()
    return render_template("index.html", user=user, countries_visited = countries_visited, countries_to_visit=countries_to_visit, cities_to_visit=cities_to_visit)

# SHOW
# GET '/country/<id>
# Show country visited and cities visited in it
@destination_blueprint.route("/country/<country_id>")
def show_country(country_id):
    country_visited = country_repository.select(country_id)
    cities_visited = city_repository.select_all_visited_from_country(country_id)
    user= user_repository.select_all()[0]
    return render_template("country.html", country = country_visited, cities_visited = cities_visited, user=user)

# SHOW 
# GET
# Show country visited
@destination_blueprint.route("/city/<city_id>")
def show_city(city_id):
    city_visited = city_repository.select(city_id)
    user = user_repository.select_all()[0]
    return render_template("city.html", city = city_visited, user = user)

# CREATE
# POST '/'
# Creates new instance of a country and adds it to visited or to visit countries 
@destination_blueprint.route("/add_country", methods=['POST'])
def add_country():
    name = request.form['name']
    user_id = request.form['user_id']
    visited = request.form['visited']

    user = user_repository.select(user_id)
    country = Country(name, user, visited) 
    country_repository.save(country)
    return redirect('/')

# CREATE
# POST '/add_city'
# Creates new instance of city anf adds it to visited or to visit cities
@destination_blueprint.route("/add_city", methods=['POST'])
def add_city():
    name = request.form['name']
    country_id = request.form['country_id']
    user_id = request.form['user_id']
    visited = request.form['visited']

    country = country_repository.select(country_id)
    user = user_repository.select(user_id)
    city = City(name, country, user, visited)
    city_repository.save(city)
    return redirect('/')