class Country:

    def __init__(self, name, user, visited = False, id = None):
        self.name = name 
        self.user = user
        self.visited = visited
        self.id = id
        self.cities = []
