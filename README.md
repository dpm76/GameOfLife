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

## 🧩 Software Design, Architecture & Best Practices

### Overview

This project is structured with a clear separation of concerns:

| Layer                       | Directory | Responsibility                                 |
| --------------------------- | --------- | ---------------------------------------------- |
| **Game Logic**              | `/game`   | Cell state management and Conway's rules       |
| **User Interface**          | `/ui`     | Console and Tkinter GUI visualization          |
| **Application Entry Point** | `main.py` | Command-line parsing and runtime configuration |

This modular architecture allows the UI to evolve independently from the game engine—for example, adding a web or mobile UI without modifying the core simulation logic.

---

### 🎯 Domain-Driven Entities

The simulation is based on two core domain objects:

| Class           | Type                     | Responsibility                                              |
| --------------- | ------------------------ | ----------------------------------------------------------- |
| `Cell`          | Value Object             | Represents a living cell in the infinite grid               |
| `CandidateCell` | Specialized Value Object | Used temporarily during evolution to compute survival/birth |

The board (`Board`) receives and produces lists of these entities each turn, applying Conway's Game of Life rules.

---

### 🧠 Design Patterns & Engineering Principles Applied

| Pattern / Principle                | Location                                 | Benefit                                              |
| ---------------------------------- | ---------------------------------------- | ---------------------------------------------------- |
| **Value Object Pattern**           | `Cell`                                   | Coordinates define identity; correct equality checks |
| **Inheritance for Specialization** | `CandidateCell(Cell)`                    | Extends state only when required for evolution       |
| **Transient Entity Pattern**       | `CandidateCell`                          | Exists only during a single turn → memory efficiency |
| **Spatial Hashing**                | `Cell.create_hash()`                     | Efficient O(1) lookup in sparse infinite grid        |
| **Separation of Concerns**         | `/game` vs `/ui`                         | Core logic isolated from rendering concerns          |
| **Dependency Inversion Principle** | UI depends on interfaces (Board results) | Easy to test and replace UI                          |
| **Encapsulation**                  | Private attributes                       | Protects internal state from external mutation       |
| **Command-Line Interface Pattern** | `main.py`                                | Encourages flexible and scriptable usage             |

---

### 🧪 Testing & Maintainability

Unit tests included in `/test` help ensure reliable behaviors:

* correct cell identity and hashing
* accurate neighbor generation
* validated rule execution in `Board`

Designed for:

* fast execution
* deterministic output
* TDD-friendly iteration

---

### ⚙️ Performance Considerations

| Optimization                                  | Result                                      |
| --------------------------------------------- | ------------------------------------------- |
| Only living cells are stored between turns    | Takes advantage of sparse grids             |
| Only neighbors of living cells are considered | Avoids scanning infinite grid               |
| Spatial hashing for identity                  | Simplifies comparisons and dictionary usage |

These techniques allow **infinite board simulation** without large memory structures.

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
python main.py initial_states/glider --mode console
python main.py initial_states/gosper_glider_gun --mode gui
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

## 🚀 Possible Future Enhancements

* Support alternative rule sets (e.g., HighLife, Seeds…)
* Parallelization or chunk-based updates
* Web or GPU rendering (Canvas / WebGL)
* Support for RLE pattern format (community standard)

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
