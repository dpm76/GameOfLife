import unittest

from game.board import Board
from game.cell import Cell


class BoardTests(unittest.TestCase):

    def test_emptyCellHas2SurroundingCells_afterPlayTurn_cellIsAlive(self):

        board = Board()
        board.set_cells([Cell(0, 0), Cell(0, 1), Cell(1, 0)])

        cells = board.play_turn()

        self.assertIn(Cell(0, 0), cells)

    def test_emptyCellHas3SurroundingCells_afterPlayTurn_cellIsAlive(self):

        board = Board()
        board.set_cells([Cell(0, 0), Cell(0, 1), Cell(1, 0), Cell(1, 1)])

        cells = board.play_turn()

        self.assertIn(Cell(0, 0), cells)

    def test_emptyCellHas0SurroundingCells_afterPlayTurn_cellIsNotAlive(self):

        board = Board()
        board.set_cells([Cell(0, 0)])

        cells = board.play_turn()

        self.assertNotIn(Cell(0, 0), cells)

    def test_emptyCellHas1SurroundingCells_afterPlayTurn_cellIsNotAlive(self):

        board = Board()
        board.set_cells([Cell(0, 0), Cell(1, 0)])

        cells = board.play_turn()

        self.assertNotIn(Cell(0, 0), cells)

    def test_emptyCellHas4SurroundingCells_afterPlayTurn_cellIsNotAlive(self):

        board = Board()
        board.set_cells([Cell(0, 0), Cell(1, 0), Cell(1, 1), Cell(0, 1), Cell(-1, 0)])

        cells = board.play_turn()

        self.assertNotIn(Cell(0, 0), cells)

    def test_emptyCellHas5SurroundingCells_afterPlayTurn_cellIsNotAlive(self):
        board = Board()
        board.set_cells([Cell(0, 0), Cell(1, 0), Cell(1, 1), Cell(0, 1),
                         Cell(-1, 0), Cell(-1, -1)])

        cells = board.play_turn()

        self.assertNotIn(Cell(0, 0), cells)

    def test_emptyCellHas6SurroundingCells_afterPlayTurn_cellIsNotAlive(self):
        board = Board()
        board.set_cells([Cell(0, 0), Cell(1, 0), Cell(1, 1), Cell(0, 1),
                         Cell(-1, 0), Cell(-1, -1), Cell(0, -1)])

        cells = board.play_turn()

        self.assertNotIn(Cell(0, 0), cells)

    def test_emptyCellHas7SurroundingCells_afterPlayTurn_cellIsNotAlive(self):
        board = Board()
        board.set_cells([Cell(0, 0), Cell(1, 0), Cell(1, 1), Cell(0, 1),
                         Cell(-1, 0), Cell(-1, -1), Cell(0, -1), Cell(-1, 1)])

        cells = board.play_turn()

        self.assertNotIn(Cell(0, 0), cells)

    def test_emptyCellHas8SurroundingCells_afterPlayTurn_cellIsNotAlive(self):
        board = Board()
        board.set_cells([Cell(0, 0), Cell(1, 0), Cell(1, 1), Cell(0, 1),
                         Cell(-1, 0), Cell(-1, -1), Cell(0, -1), Cell(-1, 1), Cell(1, -1)])

        cells = board.play_turn()

        self.assertNotIn(Cell(0, 0), cells)


if __name__ == '__main__':
    unittest.main()
