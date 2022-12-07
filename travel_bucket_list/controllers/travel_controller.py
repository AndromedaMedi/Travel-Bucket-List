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
    countries = country_repository.select_all()
    return render_template("index.html", user=user, 
        countries_visited = countries_visited, 
        countries_to_visit=countries_to_visit, 
        cities_to_visit=cities_to_visit, 
        countries=countries)

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
# GET '/city/<city_id>'
# SET city_visited = city ID from URL
# SET user = first user in database
# return country.html template passing in city_visited and user
@destination_blueprint.route("/city/<city_id>")
def show_city(city_id):
    city_visited = city_repository.select(city_id)
    user = user_repository.select_all()[0]
    return render_template("city.html", city = city_visited, user = user)


# CREATE
# POST '/add_country'
# Creates new instance of a country and adds it to visited or to visit countries 
@destination_blueprint.route("/add_country", methods=['POST'])
def add_country():
    name = request.form['name']
    user_id = request.form['user_id']
    visited = 'visited' in request.form
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
    visited = 'visited' in request.form 
    user = user_repository.select(user_id)
    country = country_repository.select(country_id)
    city = City(name, country, user, visited)
    city_repository.save(city)
    return redirect('/')



@destination_blueprint.route("/country/<country_id>/delete", methods=['POST'])
def remove_country(country_id):
    country_repository.delete(country_id)
    return redirect('/')

@destination_blueprint.route("/country/delete", methods=['POST'])
def remove_country_to_visit():
    country_id = request.form["country_id"]
    country_repository.delete(country_id)
    return redirect(request.referrer)

@destination_blueprint.route("/country/<country_id>/edit", methods=['POST'])
def update_country(country_id):
    country_to_update = country_repository.select(country_id)
    country_to_update.visited = True
    country_repository.update(country_to_update)
    return redirect('/')


@destination_blueprint.route("/city/<city_id>/delete", methods=['POST'])
def remove_city(city_id):
    deleted_city = city_repository.delete(city_id)
    return redirect(f'/country/{deleted_city.country.id}')

@destination_blueprint.route("/city/delete", methods=['POST'])
def remove_city_to_vist():
    city_id = request.form["city_id"]
    city_repository.delete(city_id)
    return redirect(request.referrer)

@destination_blueprint.route("/city/<city_id>/edit", methods=['POST'])
def update_city(city_id):
    city_to_update = city_repository.select(city_id)
    city_to_update.visited = True
    city_repository.update(city_to_update)
    return redirect('/')


@destination_blueprint.route("/delete_destination")
def show_delete_destination():
    user = user_repository.select_all()[0]
    countries = country_repository.select_all()
    cities = city_repository.select_all()
    return render_template("delete.html", user=user, countries=countries, cities=cities)



