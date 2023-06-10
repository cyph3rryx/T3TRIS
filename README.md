# Terminal T3TRIS

This is a console-based implementation of the classic game Tetris using the curses library in Python. The game features falling tetromino shapes that the player must manipulate to create complete lines and score points.

## Features

- Random selection of tetromino shapes and colors.
- Movement of tetromino shapes horizontally using arrow keys.
- Instant dropping of tetromino shapes using the down arrow key.
- Automatic merging and clearing of completed lines.
- Score tracking.

## Prerequisites

    - Python 3.x
    - curses library (usually included in Python standard library)

## How to Run

1. Make sure you have Python installed on your system.
2. Clone this repository or download the `tetris.py` file.
3. Open a terminal or command prompt and navigate to the directory where the `tetris.py` file is located.
4. Run the command `python tetris.py` to start the game.

## Gameplay

- Use the left and right arrow keys to move the tetromino shape horizontally.
- Press the down arrow key to instantly drop the tetromino shape to the bottom.
- The objective is to complete horizontal lines by arranging the tetromino shapes, which will clear the lines and earn points.
- The game ends when the stacked tetromino shapes reach the top of the screen.

## Customization

- You can modify the `board_width` and `board_height` variables in the code to change the size of the game board.
- Additional customization options can be explored by modifying the tetromino shapes, colors, or game logic within the code.
