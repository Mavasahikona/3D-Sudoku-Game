# 3D Sudoku Game

A 3D Sudoku game with score tracking, difficulty settings, and interactive gameplay.

## Features
- **3D Sudoku Grid**: Play Sudoku across three layers of 9x9 grids.
- **Score Tracking**: Track your score and save it to a local SQLite database.
- **Difficulty Settings**: Choose between Easy, Medium, and Hard difficulty levels.
- **Interactive UI**: Click to select cells and input numbers.

## Technologies Used
- Python
- Pygame
- NumPy
- SQLite

## Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Mavasahikona/3D-Sudoku-Game.git
   ```
2. **Install Dependencies**:
   ```bash
   pip install pygame numpy
   ```
3. **Run the Game**:
   ```bash
   python main.py
   ```

## Usage
- Click on a cell to select it.
- Press a number key (1-9) to fill the selected cell.
- Your score increases with each valid input.
- The difficulty can be changed in the code (default is "Easy").

## License
MIT