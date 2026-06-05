# Day 84 – Tic Tac Toe Game ⭕❌

A modern Desktop Tic Tac Toe game built with a Graphical User Interface (GUI). It features a smart game logic engine to
determine wins or draws and dynamically responds to player interactions.

## Features

- **Interactive Matrix Grid:** Responsive 3x3 grid using buttons that locked down upon selection to prevent
  double-clicking.
- **Dynamic Theming:** Smoothly alternates colors between player 'X' and player 'O' on the board
  layout.
- **Smart Validation Engine:** Scans all rows, columns, and diagonals in real-time to detect winning patterns or a
  sudden draw state.
- **Instant Board Reset:** Clears game state, flushes the back-end data matrix, and resets the visual markers back to
  defaults seamlessly.

## Tech Stack

- Python 3
- **CustomTkinter:** Modern dark/light adaptive desktop UI components.
- **Object-Oriented Programming (OOP):** Decoupled architecture separating the game presentation layer (`main.py`) from
  the rule engine processing data (`logic.py`).

## How to Run

```bash
pip install customtkinter
python main.py
```