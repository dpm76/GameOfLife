import unittest

from game.cell import Cell


class CellTests(unittest.TestCase):

    def test_cellInTopLeftQuadrant_getHash_isIn1Quadrant(self):

        cell = Cell(-1, -1)

        self.assertTrue(cell.get_hash().startswith("0"))

    def test_cellInTopRightQuadrant_getHash_isIn3Quadrant(self):

        cell = Cell(1, 1)

        self.assertTrue(cell.get_hash().startswith("3"))

    def test_cellInBottomRightQuadrant_getHash_isIn2Quadrant(self):

        cell = Cell(1, -1)

        self.assertTrue(cell.get_hash().startswith("2"))

    def test_cellInBottomLeftQuadrant_getHash_isIn0Quadrant(self):

        cell = Cell(-1, -1)

        self.assertTrue(cell.get_hash().startswith("0"))

    def test_twoCellsWithSameCoordinates_checkEqual_areEqual(self):

        cell1 = Cell(2, 4)
        cell2 = Cell(2, 4)

        self.assertTrue(cell1 == cell2)

    def test_arrayOfCells_checkExistingCell_cellIsInArray(self):

        cells = [Cell(1, 2), Cell(1, 5), Cell(-4, 5), Cell(-1, -1)]
        cell = Cell(-4, 5)

        self.assertIn(cell, cells)

    def test_arrayOfCells_checkNonExistingCell_cellIsNotInArray(self):

        cells = [Cell(1, 2), Cell(1, 5), Cell(-4, 5), Cell(-1, -1)]
        cell = Cell(-8, 10)

        self.assertNotIn(cell, cells)

    def test_cellAtCenter_getSurroundingCoords_surroundingCoordsAreReturned(self):

        cell = Cell(0, 0)
        surrounding_coords = cell.get_surrounding_coords()

        for coord in surrounding_coords:
            self.assertIn(coord, ((-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)))

    def test_cellAt12_2AndCellAt1_22_createHash_hashAreDifferent(self):

        hash1 = Cell.create_hash(12, 2)
        hash2 = Cell.create_hash(1, 22)

        self.assertNotEqual(hash1, hash2)


if __name__ == '__main__':
    unittest.main()
