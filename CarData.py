class CarData:
    def __init__(self):
        self.query = None
        self.make = "Toyota"
        self.model = "Highlander"
        self.year = 2024
        self.color = "Black"

    def car_constructor(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def car_insert(self):
        self.query = f"INSERT INTO cars VALUES (%s, %s, %s, %s);"
        return self.query

    def car_select(self):
        self.query = "SELECT * FROM cars;"
        return self.query

    def car_delete(self):
        self.query = (f"DELETE FROM cars "
                      f"WHERE make= %s;")
        return self.query
