import unittest

from game.cell import Cell
from test.ui.array_board_reader import ArrayBoardReader


class TextBoardReaderTests(unittest.TestCase):

    def test_havingInputText_afterRead_cellsAreCreated(self):

        board_reader = ArrayBoardReader([
            "0,2",
            "*",
            "**",
            "*"
        ])

        cells = board_reader.read()

        for expected_cell in (Cell(0, 2), Cell(0, 1), Cell(1, 1), Cell(0, 0)):
            self.assertIn(expected_cell, cells)


if __name__ == '__main__':
    unittest.main()
