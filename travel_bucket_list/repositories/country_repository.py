from db.run_sql import run_sql
from models.country import Country
import repositories.user_repository as user_repository


def save(country):
    sql = "INSERT INTO countries (name, user_id, visited) VALUES (%s, %s, %s) RETURNING *"
    values = [country.name, country.user.id, country.visited]
    results = run_sql(sql, values)
    id = results[0]['id']
    country.id = id
    return country

def select_all():
    countries = []
    sql = "SELECT * FROM countries"
    results = run_sql(sql)
    for row in results:
        user = user_repository.select(row['user_id'])
        country = Country(row['name'], user, row['visited'], row['id'])
        countries.append(country)
    return countries

def select_all_visited():
    countries_visited = []
    sql = "SELECT * FROM countries WHERE visited = true"
    results = run_sql(sql)
    for row in results:
        user = user_repository.select(row['user_id'])
        country = Country(row['name'], user, row['visited'], row['id'])
        countries_visited.append(country)
    return countries_visited

def select_all_to_visit():
    countries_to_visit = []
    sql = "SELECT * FROM countries WHERE visited = false"
    results = run_sql(sql)
    for row in results:
        user = user_repository.select(row['user_id'])
        country = Country(row['name'], user, row['visited'], row['id'])
        countries_to_visit.append(country)
    return countries_to_visit

def select(id):
    country = None
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result:
        user = user_repository.select(result['user_id'])
        country = Country(result['name'], user, result['visited'], result['id'])
    return country

def delete_all():
    sql = "DELETE FROM countries"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(country):
    sql = "UPDATE countries SET (name, user_id, visited) = (%s, %s, %s) WHERE id = %s"
    values = [country.name, country.user.id, country.visited, country.id]
    run_sql(sql, values)
