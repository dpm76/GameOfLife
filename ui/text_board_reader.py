import re as regex

from abc import ABC, abstractmethod

from game.cell import Cell


class TextBoardReader(ABC):

    @abstractmethod
    def _read_next_line(self):
        pass

    def read(self):

        cells = []

        line = self._read_next_line()
        chunks = regex.findall(r"\d+", line.strip())
        ref_coord = int(chunks[0]), int(chunks[1])

        y = ref_coord[1]
        line = self._read_next_line()
        while line is not None:
            x = ref_coord[0]
            for char in line.rstrip():
                if char == "*":
                    cells.append(Cell(x, y))
                x += 1

            y -= 1
            line = self._read_next_line()

        return cells
