import tkinter as tk

from ui.board_viewer import BoardViewer

class GuiBoardViewer(BoardViewer):
    default_width = 500
    default_height = 500
    default_padding = 0
    default_background_color = "white"
    default_foreground_color = "blue"

    def _do_after_set_window_no_grid(self):

        num_columns = self._right_bottom[0] - self._left_top[0] + 1
        self.__column_width = GuiBoardViewer.default_width / num_columns

        num_rows = self._left_top[1] - self._right_bottom[1] + 1
        self.__row_height = GuiBoardViewer.default_height / num_rows

    def _do_after_set_window_with_grid(self):
        """
        Shows board with grid
        """

        self.__canvas.create_line((1, 0), (1, GuiBoardViewer.default_height), width=1,
                                  fill=GuiBoardViewer.default_foreground_color)
        num_columns = self._right_bottom[0] - self._left_top[0] + 1
        self.__column_width = GuiBoardViewer.default_width / num_columns
        col_border = self.__column_width
        while col_border < GuiBoardViewer.default_width:
            x = int(round(col_border))
            self.__canvas.create_line((x, 0), (x, GuiBoardViewer.default_height), width=1,
                                      fill=GuiBoardViewer.default_foreground_color)
            col_border += self.__column_width

        self.__canvas.create_line((0, 1), (GuiBoardViewer.default_width, 1), width=1,
                                  fill=GuiBoardViewer.default_foreground_color)
        num_rows = self._left_top[1] - self._right_bottom[1] + 1
        self.__row_height = GuiBoardViewer.default_height / num_rows
        row_border = self.__row_height
        while row_border < GuiBoardViewer.default_height:
            y = int(round(row_border))
            self.__canvas.create_line((0, y), (GuiBoardViewer.default_width, y), width=1,
                                      fill=GuiBoardViewer.default_foreground_color)
            row_border += self.__row_height

    def __init__(self):

        super().__init__()
        self.__root = tk.Tk()
        self.__root.title("Game of Life")

        self.__canvas = tk.Canvas(self.__root,
                                  width=GuiBoardViewer.default_width,
                                  height=GuiBoardViewer.default_height,
                                  bg=GuiBoardViewer.default_background_color)
        self.__canvas.pack(anchor=tk.CENTER, expand=True)

        self.__row_height = 0.0
        self.__column_width = 0.0
        
        self.__rectangles = dict()
        
        self._do_after_set_window_delegate = self._do_after_set_window_no_grid
        
    def use_grid(self, use_grid):
    
        if use_grid:
            self._do_after_set_window_delegate = self._do_after_set_window_with_grid
        
        return self
        
    def _do_after_set_window(self):
        self._do_after_set_window_delegate()

    def _clear_viewer(self):
        pass

    def _display_cell(self, cell, is_alive):

        if is_alive:
            x0 = int(round((cell.coord[0] - self._left_top[0]) * self.__column_width)) + GuiBoardViewer.default_padding + 1
            x1 = int(round((cell.coord[0] - self._left_top[0] + 1) * self.__column_width)) - GuiBoardViewer.default_padding
            y0 = int(round((self._left_top[1] - cell.coord[1]) * self.__row_height)) + GuiBoardViewer.default_padding + 1
            y1 = int(round((self._left_top[1] - cell.coord[1] + 1) * self.__row_height)) - GuiBoardViewer.default_padding

            self.__rectangles[cell.get_hash()] = self.__canvas.create_rectangle(x0, y0, x1, y1,
                                           fill=GuiBoardViewer.default_foreground_color,
                                           width=0)
        else:
            self.__canvas.delete(self.__rectangles.pop(cell.get_hash()))

    def _do_after_display(self):
        pass

    def do_loop(self):

        return self.__root.mainloop()
