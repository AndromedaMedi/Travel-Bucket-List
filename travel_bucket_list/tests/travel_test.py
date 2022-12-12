import unittest
from models.user import User
from models.country import Country
from models.city import City

class TestTravel(unittest.TestCase):
    def setUp(self):
        self.user = User("Chloe Adams", 25)
        self.country = Country("Greece", "Chloe Adams", True)
        self.city = City("Athens", "Greece", "Chloe Adams", False)



    def test_user_has_name(self):
        self.assertEqual("Chloe Adams", self.user.name)


    def test_country_is_visited(self):
        self.assertEqual(True, self.country.visited)
    