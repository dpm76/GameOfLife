from threading import Thread
from time import sleep
from game.board import Board


class GameOfLifeRunner:

    def __init__(self, board_reader, board_viewer):

        self._board = Board()
        self._board_reader = board_reader
        self._board_viewer = board_viewer
        self._playing_thread = Thread(target=self._play, daemon=True)
        self._is_running = False

    def _play(self):

        while not self._is_running:
            sleep(0.5)

        while self._is_running:
            self._board_viewer.display(self._board.play_turn())
            sleep(0.25)

    def initialise(self):

        cells = self._board_reader.read()
        self._board.set_cells(cells)
        self._board_viewer.display(cells)

        return self

    def run(self):

        self._playing_thread.start()
        self._is_running = True
        self._board_viewer.do_loop()
        self._is_running = False
