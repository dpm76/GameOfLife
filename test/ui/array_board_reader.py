from ui.text_board_reader import TextBoardReader


class ArrayBoardReader(TextBoardReader):

    def __init__(self, lines):

        self.__lines = lines
        self.__current_line = 0

    def _read_next_line(self):

        if len(self.__lines) > self.__current_line:
            line = self.__lines[self.__current_line]
            self.__current_line += 1
            return line

        return None
