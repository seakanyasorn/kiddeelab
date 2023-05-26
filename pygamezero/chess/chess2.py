# Import Pygame Zero library
import pgzrun

# Set the screen size
WIDTH = 600
HEIGHT = 600

# Set the board size and spacing
BOARD_SIZE = 8
SPACING = WIDTH // BOARD_SIZE
# Define the selected piece variable
selected_piece = None

# Define the chess pieces
PAWN = "pawn"
ROOK = "rook"
KNIGHT = "knight"
BISHOP = "bishop"
QUEEN = "queen"
KING = "king"

# Define the starting position of the pieces
START_POSITION = {
    "a1": ROOK,
    "b1": KNIGHT,
    "c1": BISHOP,
    "d1": QUEEN,
    "e1": KING,
    "f1": BISHOP,
    "g1": KNIGHT,
    "h1": ROOK,
    "a2": PAWN,
    "b2": PAWN,
    "c2": PAWN,
    "d2": PAWN,
    "e2": PAWN,
    "f2": PAWN,
    "g2": PAWN,
    "h2": PAWN,
    "a7": PAWN,
    "b7": PAWN,
    "c7": PAWN,
    "d7": PAWN,
    "e7": PAWN,
    "f7": PAWN,
    "g7": PAWN,
    "h7": PAWN,
    "a8": ROOK,
    "b8": KNIGHT,
    "c8": BISHOP,
    "d8": QUEEN,
    "e8": KING,
    "f8": BISHOP,
    "g8": KNIGHT,
    "h8": ROOK,
}

# Define the chess board
board = {}

# Initialize the board
for row in range(BOARD_SIZE):
    for col in range(BOARD_SIZE):
        x = col * SPACING
        y = row * SPACING
        board[(col, row)] = None

# Set the starting position of the pieces on the board
for position, piece in START_POSITION.items():
    col, row = ord(position[0]) - ord('a'), int(position[1]) - 1
    board[(col, row)] = piece

# Define the function to draw the board
def draw_board():
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            x = col * SPACING
            y = row * SPACING
            if (row + col) % 2 == 0:
                screen.draw.filled_rect(Rect(x, y, SPACING, SPACING), "white")
            else:
                screen.draw.filled_rect(Rect(x, y, SPACING, SPACING), "gray")

# Define the function to draw the pieces
# Define the function to draw the pieces
def draw_pieces():
    for position, piece in START_POSITION.items():
        col, row = ord(position[0]) - ord('a'), int(position[1]) - 1
        x = col * SPACING + SPACING // 5
        y = row * SPACING + SPACING // 5
        filename = f"w_{piece}.png"
        if row < 2:
            # Black pieces
            filename = f"b_{piece}.png"
        screen.blit(filename, (x, y))

def highlight_valid_moves(selected_piece):
    valid_moves = calculate_valid_moves(selected_piece)
    for move in valid_moves:
        col, row = move
        x = col * SPACING + SPACING // 2
        y = row * SPACING + SPACING // 2
        screen.draw.circle((x, y), SPACING // 4, "yellow")

# Define the function to clear the highlighted moves
def clear_highlighted_moves():
    global board
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if (row + col) % 2 == 0:
                color = "white"
            else:
                color = "gray"
            screen.draw.filled_rect(Rect(col * SPACING, row * SPACING, SPACING, SPACING), color)
            piece = board[(col, row)]
            if piece is not None:
                x = col * SPACING + SPACING // 5
                y = row * SPACING + SPACING // 5
                filename = f"w_{piece}.png"
                if row < 2:
                    # Black pieces
                    filename = f"b_{piece}.png"
                screen.blit(filename, (x, y))

def is_valid_position(col, row):
    """
    Check if the given column and row values represent a valid position on the board.
    """
    return 0 <= col < BOARD_SIZE and 0 <= row < BOARD_SIZE

def get_piece_color(piece):
    if piece is None:
        return None
    elif piece[0] == 'w':
        return 'white'
    elif piece[0] == 'b':
        return 'black'

def calculate_valid_moves(piece, position):
    col, row = position
    piece = board[position]

    if piece == PAWN:
        valid_moves = []

        # Determine the direction the pawn moves based on its color
        if row < BOARD_SIZE // 2:
            direction = 1  # White pawns move up
        else:
            direction = -1  # Black pawns move down

        # Check the square in front of the pawn
        new_position = (col, row + direction)
        if is_valid_position(new_position) and board[new_position] is None:
            valid_moves.append(new_position)

            # Check the square two spaces in front of the pawn if it hasn't moved yet
            if (row == 1 and direction == 1) or (row == BOARD_SIZE - 2 and direction == -1):
                new_position = (col, row + 2 * direction)
                if is_valid_position(new_position) and board[new_position] is None:
                    valid_moves.append(new_position)

        # Check the two diagonal squares for capturing
        for d_col in [-1, 1]:
            new_position = (col + d_col, row + direction)
            if is_valid_position(new_position) and board[new_position] is not None:
                if get_piece_color(board[new_position]) != get_piece_color(piece):
                    valid_moves.append(new_position)

        return valid_moves


def on_mouse_down(pos):
    global selected_piece
    col = pos[0] // SPACING
    row = pos[1] // SPACING
    piece = board[(col, row)]

    if piece:
        selected_piece = (col, row)
        # Calculate valid moves for the selected piece
        valid_moves = calculate_valid_moves(piece, (col, row))
        # Highlight the valid moves on the board
        highlight_valid_moves(valid_moves)
    elif selected_piece:
        # Check if the selected square is a valid move
        if (col, row) in valid_moves:
            # Move the selected piece to the new position
            board[(col, row)] = board[selected_piece]
            board[selected_piece] = None
            selected_piece = None
        else:
            # Deselect the piece if the move is not valid
            selected_piece = None
            # Clear the highlighted valid moves on the board
            clear_highlighted_moves()

# Define the main function to run the game
def update():
    pass

def draw():
    draw_board()
    draw_pieces()

# Run the game
pgzrun.go()
