from ui.text_board_reader import TextBoardReader


class FileBoardReader(TextBoardReader):

    def __init__(self, file_name):

        self.__input_file = open(file_name, 'r')

    def _read_next_line(self):

        line = self.__input_file.readline()
        return line if line else None

    def __del__(self):

        self.__input_file.close()
