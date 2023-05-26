import pygame
import pygame.freetype
import pgzrun

WIDTH = 400
HEIGHT = 400

# Define the game board
board = [[None]*8 for _ in range(8)]
pawn_white = False
move_pawn_white = False


class Piece:
    def __init__(self, piece_type, color, x, y):
        self.piece_type = piece_type
        self.color = color
        self.x = x
        self.y = y
    def draw(self):
        x_pos = self.x * 50 +7.5
        y_pos = self.y * 50 
        #screen.draw.filled_circle((x_pos, y_pos), 20, self.color )
        if self.piece_type == 'pawn':
            if self.color == 'white':
                screen.blit('pawn_white', (x_pos, y_pos))
            elif self.color == 'black':
                screen.blit('pawn_black', (x_pos, y_pos))
        # elif self.piece_type == 'rook':
        #     if self.color == 'white':
        #         screen.blit('rook_white', (x_pos, y_pos))
        #     elif self.color == 'black':
        #         screen.blit('rook_black', (x_pos, y_pos))

# Create the pieces
for i in range(8):
    board[1][i] = Piece('pawn', 'white', i, 1)
    board[6][i] = Piece('pawn', 'black', i, 6)
# board[0][0] = Piece('rook', 'white', 0, 0)
# board[0][7] = Piece('rook', 'white', 7, 0)
# board[7][0] = Piece('rook', 'black', 0, 7)
# board[7][7] = Piece('rook', 'black', 7, 7)

    

# Define the event loop
def on_mouse_down(pos): 
    global pawn_white,x_pawn_white,y_pawn_white,move_pawn_white,y_pawn_new
    x = pos[0] // 50
    y = pos[1] // 50
    if board[y][x] is not None:
        print(board[y][x].piece_type)
        if board[y][x].piece_type == 'pawn':
            if board[y][x].color == 'white':
                x_pawn_white = x
                y_pawn_white = y
                pawn_white = True
    if pawn_white and y == y_pawn_white+1:
        board[y_pawn_white][x_pawn_white] = None
        board[y][x] = Piece('pawn', 'white', x, y)
    
def move_pawn(x, y):
    global pawn_white, x_pawn_white, y_pawn_white, move_pawn_white
    if (y == y_pawn_white + 1) and (x == x_pawn_white) and (board[y][x] is None):
        board[y_pawn_white][x_pawn_white] = None
        board[y][x] = Piece('pawn', 'white', x, y)
    elif (y == y_pawn_white + 2) and (x == x_pawn_white) and (board[y-1][x] is None) and (board[y][x] is None) and (y_pawn_white == 1):
        board[y_pawn_white][x_pawn_white]

# Define the draw function
def draw():
    for y in range(8):
        for x in range(8):
            if (x + y) % 2 == 0:
                color = (0, 0, 0)  # green
            else:
                color = (255, 255, 255) 
            Box = Rect ((x*50, y*50), (50, 50))
            screen.draw.filled_rect(Box,color)
    for i in range(8):
        board[1][i].draw() 
        board[6][i].draw()
    if pawn_white:
        for y_w_pawn in range(y_pawn_white+1,y_pawn_white+3):
            Box = Rect ((x_pawn_white*50, y_w_pawn*50), (50, 50))
            screen.draw.filled_rect(Box,'yellow')
            print(1)
  
  
 

            

pgzrun.go()
