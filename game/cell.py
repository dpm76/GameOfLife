class Cell:

    @staticmethod
    def create_hash(x, y):
        quadrant = (2 if x >= 0 else 0) + (1 if y >= 0 else 0)
        return f"{quadrant}_{abs(x)}_{abs(y)}"

    def __init__(self, x, y):

        self.coord = (x, y)
        self.__hash = Cell.create_hash(x, y)

    def __str__(self):

        return f"({self.coord[0]}, {self.coord[1]})"

    def get_hash(self):

        return self.__hash

    def __eq__(self, other):

        return self.coord[0] == other.coord[0] and self.coord[1] == other.coord[1]

    def get_surrounding_coords(self):

        return (
            (self.coord[0] - 1, self.coord[1] + 1),
            (self.coord[0], self.coord[1] + 1),
            (self.coord[0] + 1, self.coord[1] + 1),
            (self.coord[0] - 1, self.coord[1]),
            (self.coord[0] + 1, self.coord[1]),
            (self.coord[0] - 1, self.coord[1] - 1),
            (self.coord[0], self.coord[1] - 1),
            (self.coord[0] + 1, self.coord[1] - 1),
        )
