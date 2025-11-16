import argparse

from game_of_life_runner import GameOfLifeRunner
from sys import modules
from ui.console_board_viewer import ConsoleBoardViewer
from ui.file_board_reader import FileBoardReader
try:
    from ui.gui_board_viewer import GuiBoardViewer
except Exception as ex:
    print(f"Warning: {ex}")


def main():

    parser = argparse.ArgumentParser(prog="Game of Life", description="Another implementation of the Game of Life")
    parser.add_argument("filename", help="Initial state file")

    gui_available = "ui.gui_board_viewer" in modules
    if gui_available:
        parser.add_argument("--mode", default="gui", nargs="?", choices=["console", "gui", "grid"],
                        help="Let it run either in console or in GUI application mode (default: %(default)s)")
    else:
        print("GUI not available!")

    args = parser.parse_args()

    if not gui_available or args.mode == "console":
        viewer = ConsoleBoardViewer().set_window((-10, 10), (10, -10))
    else:
        viewer = GuiBoardViewer().use_grid(args.mode == "grid").set_window((-60, 60), (60, -60))

    GameOfLifeRunner(FileBoardReader(args.filename), viewer).initialise().run()


if __name__ == '__main__':
    main()
