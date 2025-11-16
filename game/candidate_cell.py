from game.cell import Cell


class CandidateCell(Cell):

    def __init__(self, x, y):

        super().__init__(x, y)
        self.__surrounding_cells_count = 0
        self.__last_state_alive = False

    def inc_surrounding_cells_count(self):

        self.__surrounding_cells_count += 1

    def get_surrounding_cells_count(self):

        return self.__surrounding_cells_count

    def set_last_state_alive(self):

        self.__last_state_alive = True

    def last_state_is_alive(self):

        return self.__last_state_alive
