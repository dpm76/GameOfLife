from ui.board_viewer import BoardViewer


class ConsoleBoardViewer(BoardViewer):

    def _do_after_set_window(self):
        pass

    def __init__(self):

        super().__init__()

    def _display_cell(self, cell, is_alive):

        char = "*" if is_alive else " "
        coord = cell.coord
        if self._coord_is_within_window(coord):
            position = self._left_top[1] - coord[1] + 1, coord[0] - self._left_top[0] + 1
            print(f"\033[{position[0]};{position[1]}H{char}")

    def __go_to_bottom(self):
        print(f"\033[{self._left_top[1] - self._right_bottom[1] + 2};1H")

    def _do_after_display(self):

        self.__go_to_bottom()

    def _clear_viewer(self):

        print("\033[2J")

    def do_loop(self):

        self.__go_to_bottom()
        input("Press enter to finish")
