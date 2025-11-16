# 🧬 Game of Life – Python Implementation

A **Python implementation** of Conway’s **Game of Life** simulating the evolution of cellular automata through standard rules.
The initial state is defined in a file and the simulation can be visualized:

* in the **console**, or
* in a **GUI window** (requires `tkinter`)

---

## 📂 Project Structure

```
GameOfLife/
│
├── game/               # Core Game of Life logic
├── ui/                 # User interfaces (console / GUI)
├── initial_states/     # Sample initial state input files
├── test/               # Unit tests
├── main.py             # Application entry point
├── LICENSE
└── README.md
```

Game logic and user interface are cleanly separated across modules.

---

## ▶️ Running the Application

```bash
python main.py filename [--mode MODE]
```

### 📌 Command line arguments

| Argument                    | Description                         |
| --------------------------- | ----------------------------------- |
| `filename`                  | Path to the initial state file      |
| `--mode {console,gui,grid}` | Visualization mode (default: `gui`) |
| `-h`, `--help`              | Display help                        |

Examples:

```bash
python main.py initial_states/glider.txt --mode console
python main.py initial_states/gosper_glider_gun.txt --mode gui
```

> GUI mode requires the `tkinter` module.

---

## 🧪 Running Unit Tests

```bash
python -m unittest
```

Verbose output:

```bash
python -m unittest -v
```

---

## 🛠️ Requirements & Virtual Environment (optional)

Only **Python standard libraries** are used.

To create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

---

## 🪟 Installing tkinter

If GUI mode fails due to missing tkinter, install it using:

### Linux (Debian/Ubuntu/Raspberry Pi OS)

```bash
sudo apt-get update
sudo apt-get install python3-tk
```

### Fedora

```bash
sudo dnf install python3-tkinter
```

### Arch Linux

```bash
sudo pacman -S tk
```

### macOS & Windows

Usually included with Python from python.org.
If missing, reinstall Python using the official installer.

---

## 📌 Initial State File Format

Initial states are stored in **plain text files**:

1. **First line** → starting board coordinates
   Format:

   ```
   x, y
   ```

   Example:

   ```
   0, 0
   ```

2. Starting from the **second line**:

   * `*` → alive cell
   * space `" "` → dead cell

Cells are placed **relative to the starting coordinates**.
All rows must have the same width.

### Example: Blinker (oscillator)

```
5, 3
 *
 *
 *
```

This places the first cell of the second line at coordinate `(5,3)` and builds the pattern downward.

---

## 🌟 Famous Patterns

Some classic patterns compatible with this format:

| Pattern               | Type       | Description                   |
| --------------------- | ---------- | ----------------------------- |
| **Glider**            | Spaceship  | Moves diagonally forever      |
| **Blinker**           | Oscillator | Alternates between two states |
| **Toad**              | Oscillator | Period-2 oscillator           |
| **Gosper Glider Gun** | Gun        | Produces infinite gliders     |
| **Block**             | Still Life | Stays unchanged               |

Multiple ready-to-use samples are located in the `initial_states/` directory.

---

## 📚 Additional Resources

Learn more about Conway’s Game of Life:

* Wikipedia — Conway’s Game of Life
  [https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)
* ConwayLife.com — The Life Wiki
  [https://www.conwaylife.com/wiki/Main_Page](https://www.conwaylife.com/wiki/Main_Page)
* Play Game of Life online
  [https://playgameoflife.com/](https://playgameoflife.com/)
* Coding Train — Game of Life video tutorial
  [https://www.youtube.com/watch?v=FWSR_7kZuYg](https://www.youtube.com/watch?v=FWSR_7kZuYg)
* Original 1970 Scientific American article (Martin Gardner)
  [https://web.archive.org/web/20231101083058/http://www.ibiblio.org/lifepatterns/october1970scientificamerican.pdf](https://web.archive.org/web/20231101083058/http://www.ibiblio.org/lifepatterns/october1970scientificamerican.pdf)

---

## 📜 License

This project is open-source (under MIT license).
Contributions and improvements are welcome!
