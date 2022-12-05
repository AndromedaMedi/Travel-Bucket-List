from models.user import User
from models.country import Country
from models.city import City

import repositories.user_repository as  user_repository
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository



user_repository.delete_all()
country_repository.delete_all()
city_repository.delete_all()

user1 = User("Chloe Adams", 26)
user_repository.save(user1)

user_repository.select_all()

country1 = Country("Greece", user1, True)
country_repository.save(country1)
country2 = Country("Germany", user1, True)
country_repository.save(country2)
country3 = Country("Belgium", user1, False)
country_repository.save(country3)
country4 = Country("France", user1, True)
country_repository.save(country4)
country5 = Country("England", user1, True)
country_repository.save(country5)
country6 = Country("Scotland", user1, True)
country_repository.save(country6)
country7 = Country("Thailand", user1, False)
country_repository.save(country7)

country_repository.select_all()

city1 = City("Athens", country1, user1, False)
city_repository.save(city1)
city2 = City("Thessaloniki", country1, user1, True)
city_repository.save(city2)
city3 = City("Berlin", country2, user1, True)
city_repository.save(city3)
city4 = City("Munich", country2, user1, False)
city_repository.save(city4)
city5 = City("Brussels", country3, user1, False)
city_repository.save(city5)
city6 = City("Antwerp", country3, user1, False)
city_repository.save(city6)
city7 = City("Paris", country4, user1, False)
city_repository.save(city7)
city8 = City("Leon", country4, user1, False)
city_repository.save(city8)
city9 = City("London", country5, user1, True)
city_repository.save(city9)
city10 = City("Glasgow", country6, user1, True)
city_repository.save(city10)
city11 = City("Edinburgh", country7, user1, True)
city_repository.save(city11)
city12 = City("Patra", country1, user1, False)
city_repository.save(city12)


city_repository.select_all()


