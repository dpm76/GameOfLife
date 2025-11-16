from game.candidate_cell import CandidateCell
from game.cell import Cell


class Board:

    def __init__(self):
        self.__cells = []

    def play_turn(self):

        candidate_cells = dict()

        for cell in self.__cells:

            cell_hash = cell.get_hash()
            if cell_hash not in candidate_cells:
                candidate_cells[cell_hash] = CandidateCell(cell.coord[0], cell.coord[1])
            candidate_cells[cell_hash].set_last_state_alive()

            for coord in cell.get_surrounding_coords():

                surrounding_cell_hash = Cell.create_hash(coord[0], coord[1])
                if surrounding_cell_hash not in candidate_cells:
                    candidate_cells[surrounding_cell_hash] = CandidateCell(coord[0], coord[1])
                candidate_cells[surrounding_cell_hash].inc_surrounding_cells_count()

        self.__cells = []
        for cell in candidate_cells.values():
            if (cell.last_state_is_alive() and cell.get_surrounding_cells_count() == 2) \
                    or cell.get_surrounding_cells_count() == 3:
                self.__cells.append(cell)

        return self.__cells

    def set_cells(self, cells):
        self.__cells = cells
