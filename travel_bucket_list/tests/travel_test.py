import unittest
from models.user import User
from models.country import Country
from models.city import City

class TestTravel(unittest.TestCase):
    def setUp(self):
        self.user = User("Chloe Adams", 25)
        self.country = Country("Greece", "Chloe Adams", False)
        self.city = City("Athens", "Greece", "Chloe Adams", False)

        