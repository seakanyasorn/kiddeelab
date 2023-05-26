import pygame
import pygame.freetype
import pgzrun

WIDTH = 400
HEIGHT = 400

# Define the game board
board = [[None]*8 for _ in range(8)]
possible_moves = []

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
        elif self.piece_type == 'rook':
            if self.color == 'white':
                screen.blit('rook_white', (x_pos, y_pos))
            elif self.color == 'black':
                screen.blit('rook_black', (x_pos, y_pos))

# Create the pieces
for i in range(8):
    board[1][i] = Piece('pawn', 'white', i, 1)
    board[6][i] = Piece('pawn', 'black', i, 6)
board[0][0] = Piece('rook', 'white', 0, 0)
board[0][7] = Piece('rook', 'white', 7, 0)
board[7][0] = Piece('rook', 'black', 0, 7)
board[7][7] = Piece('rook', 'black', 7, 7)

# Define the event loop
def on_mouse_down(pos):
    global possible_moves,rook,piece
    # x = pos[0] // 50
    # y = pos[1] // 50
    # if board[y][x] is not None:
    #     board[y][x].draw()
    #     print(board[y][x].piece_type)
    
    x = pos[0] // 50
    y = pos[1] // 50
    if board[y][x] is not None:
        piece = board[y][x]
        if piece.piece_type == 'pawn':
            # Check if the pawn can move one or two squares forward
            if piece.color == 'white':
                if y == 1 and board[y+1][x] is None or board[y+1][x] is None and y != 0:
                    # Move the pawn one or two squares forward
                    board[y][x] = None
                    piece.y = y+1
                    board[y+1][x] = piece
            elif piece.color == 'black':
                if y == 6 and board[y-1][x] is None or board[y-1][x] is None and y != 7:
                    # Move the pawn one or two squares forward
                    board[y][x] = None
                    piece.y = y-1
                    board[y-1][x] = piece
        elif piece.piece_type == 'rook':
            # Handle rook movement
            # Check if the rook can move horizontally or vertically
            if piece.color == 'white':
                rook = board[y][x]
                print(rook)
                possible_moves = []
                # Check for legal moves to the left
                for i in range(x-1, -1, -1):
                    if board[y][i] is None:
                        possible_moves.append((i, y))
                    else:
                        break
                # Check for legal moves to the right
                for i in range(x+1, 8):
                    if board[y][i] is None:
                        possible_moves.append((i, y))
                    else:
                        break
                # Check for legal moves to the top
                for i in range(y-1, -1, -1):
                    if board[i][x] is None:
                        possible_moves.append((x, i))
                    else:
                        break
                # Check for legal moves to the bottom
                for i in range(y+1, 8):
                    if board[i][x] is None:
                        possible_moves.append((x, i))
                    else:
                        break
                
                x_rook_mov = pos[0] // 50
                y_rook_mov = pos[1] // 50
                # Move the rook
                print(possible_moves)
                for move in possible_moves:
                    print('ok',move)
                    print(move[0], move[1])
                    print(x_rook_mov, y_rook_mov)
                    # if move[0] == pos[0] // 50 and move[1] == pos[1] // 50:       
                    board[rook.y][rook.x] = None
                    rook.x = move[0]
                    rook.y = move[1]
                    board[rook.y][rook.x] = rook
                    break
                
            elif piece.color == 'black':
                # Handle black rook movement
                pass

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
            if board[y][x] is not None:
                board[y][x].draw()
                # Highlight possible moves
                piece = board[y][x]
                if piece.piece_type == 'rook':
                    
                    print(possible_moves)
                    for move in possible_moves:
                        Box = Rect((move[0]*50, move[1]*50), (50, 50))
                        screen.draw.filled_rect(Box, (255, 0, 0))
            
            

pgzrun.go()
