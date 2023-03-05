import curses
import random

# Initialize the game window
window = curses.initscr()
curses.curs_set(0)
window.nodelay(1)
window.timeout(100)

# Define the game variables
board_width = 20
board_height = 30
board = [[0 for x in range(board_width)] for y in range(board_height)]
score = 0

# Define the tetromino shapes
tetrominos = [    [[1, 1, 1, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 1], [1, 1]],
    [[1, 0, 0], [1, 1, 1]],
    [[0, 0, 1], [1, 1, 1]],
    [[1, 1], [0, 1], [0, 1]],
]

# Define the tetromino colors
colors = [    curses.COLOR_RED,    curses.COLOR_GREEN,    curses.COLOR_YELLOW,    curses.COLOR_BLUE,    curses.COLOR_MAGENTA,    curses.COLOR_CYAN,    curses.COLOR_WHITE,]

# Define the game functions
def draw_board():
    for y in range(board_height):
        for x in range(board_width):
            if board[y][x] == 0:
                window.addch(y, x, " ")
            else:
                window.addstr(y, x, "X", curses.color_pair(board[y][x]))

def new_piece():
    piece = random.choice(tetrominos)
    color = random.choice(colors)
    return piece, color

def draw_piece(piece, color, x, y):
    for row in range(len(piece)):
        for col in range(len(piece[row])):
            if piece[row][col] == 1:
                window.addstr(y + row, x + col, "X", curses.color_pair(color))

def erase_piece(piece, x, y):
    for row in range(len(piece)):
        for col in range(len(piece[row])):
            if piece[row][col] == 1:
                window.addstr(y + row, x + col, " ")

def check_collision(piece, x, y):
    for row in range(len(piece)):
        for col in range(len(piece[row])):
            if piece[row][col] == 1:
                if board[y + row][x + col] != 0:
                    return True
    return False

def merge_piece(piece, color, x, y):
    for row in range(len(piece)):
        for col in range(len(piece[row])):
            if piece[row][col] == 1:
                board[y + row][x + col] = color

def check_lines():
    global score
    lines_cleared = 0
    for y in range(board_height):
        if all(board[y]):
            board.pop(y)
            board.insert(0, [0 for x in range(board_width)])
            lines_cleared += 1
    score += lines_cleared ** 2

# Main game loop
while True:
    # Start a new piece if necessary
    if "piece" not in locals():
        piece, color = new_piece()
        x = board_width // 2 - len(piece[0]) // 2
        y = 0

    # Move the piece down if possible
    if not check_collision(piece, x, y + 1):
        erase_piece(piece, x, y)
        y += 1
        draw_piece(piece, color, x, y)
    else:
        merge_piece(piece, color, x, y)
        check_lines()
        del piece
        continue

    # Handle user input
    c = window.getch()
    if c == curses.KEY_LEFT and x > 0 and not check_collision(piece, x - 1, y):
        erase_piece(piece, x, y)
        x -= 1
        draw_piece(piece, color, x, y)
    elif c == curses.KEY_RIGHT and x < board_width - len(piece[0]) and not check_collision(piece, x + 1, y):
        erase_piece(piece, x, y)
        x += 1
        draw_piece(piece, color, x, y)
    elif c == curses.KEY_DOWN:
        while not check_collision(piece, x, y + 1):
            erase_piece(piece, x, y)
            y += 1
            draw_piece(piece, color, x, y)
        merge_piece(piece, color, x, y)
        check_lines()
        del piece
        continue

    # Update the screen
    draw_board()
    window.addstr(board_height + 2, 0, f"Score: {score}")

    # Check for game over
    if any(board[0]):
        break

# End the game
curses.endwin()
print(f"Game over! Final score: {score}")

