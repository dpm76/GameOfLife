from abc import ABC, abstractmethod


class BoardViewer(ABC):

    def __init__(self):

        self._left_top = (0, 0)
        self._right_bottom = (0, 0)
        self._cells = []

        self.clear()

    def _coord_is_within_window(self, coord):

        return self._left_top[0] <= coord[0] <= self._right_bottom[0] \
            and self._left_top[1] >= coord[1] >= self._right_bottom[1]

    @abstractmethod
    def _clear_viewer(self):
        pass

    def clear(self):

        self._cells = []
        self._clear_viewer()

    @abstractmethod
    def _do_after_set_window(self):
        pass

    def set_window(self, left_top, right_bottom):

        self._left_top = left_top
        self._right_bottom = right_bottom

        self._do_after_set_window()

        return self

    @abstractmethod
    def _display_cell(self, cell, is_alive):
        pass

    @abstractmethod
    def _do_after_display(self):
        pass

    def display(self, cells):

        for cell in self._cells:
            if cell not in cells:
                self._display_cell(cell, False)

        for cell in cells:
            if cell not in self._cells:
                self._display_cell(cell, True)

        self._cells = cells

        self._do_after_display()

    @abstractmethod
    def do_loop(self):
        pass
