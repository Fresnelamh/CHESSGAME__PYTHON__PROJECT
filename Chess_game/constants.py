



import pygame
import os

Width=620

Height=620

Rows=8

Cols=8

dim=8

Square=Width//Rows

#couleurs des cases du tableau
brown=(87,16,16)
Black = (0, 0, 0)
White=(255,255,255)
blue=(0, 0, 139)
red=(139, 0, 0, 0.342)

current_player_color=White
MAX_FPS=15
iMG={}
#font = pygame.font.Font('freesansbold.ttf', 20)
#medium_font = pygame.font.Font('freesansbold.ttf', 40)
#big_font = pygame.font.Font('freesansbold.ttf', 50)
timer = pygame.time.Clock()
fps = 60


Path="Chess_game/chess_images"

#Pièces noires
Black_Knight=pygame.transform.scale(pygame.image.load(os.path.join(Path,"bkn.png")), (Square,Square))
Black_Bishop=pygame.transform.scale(pygame.image.load(os.path.join(Path,"bB.png")), (Square,Square))
Black_King=pygame.transform.scale(pygame.image.load(os.path.join(Path,"bk.png")), (Square,Square))
Black_Pawn=pygame.transform.scale(pygame.image.load(os.path.join(Path,"bp.png")), (Square,Square))
Black_Queen=pygame.transform.scale(pygame.image.load(os.path.join(Path,"bq.png")), (Square,Square))
Black_Rook=pygame.transform.scale(pygame.image.load(os.path.join(Path,"br.png")), (Square,Square))

#Pièces blanches
White_Knight=pygame.transform.scale(pygame.image.load(os.path.join(Path,"wkn.png")), (Square,Square))
 
White_Bishop=pygame.transform.scale(pygame.image.load(os.path.join(Path,"wB.png")), (Square,Square))
White_King=pygame.transform.scale(pygame.image.load(os.path.join(Path,"wk.png")), (Square,Square))
White_Pawn=pygame.transform.scale(pygame.image.load(os.path.join(Path,"wp.png")), (Square,Square))
White_Queen=pygame.transform.scale(pygame.image.load(os.path.join(Path,"wq.png")), (Square,Square))
White_Rook=pygame.transform.scale(pygame.image.load(os.path.join(Path,"wr.png")), (Square,Square))


white_images = [White_Pawn, White_Queen, White_King, White_Knight, White_Rook, White_Bishop]
white_promotions = ['Bishop', 'Knight', 'Rook', 'Queen']
white_moved = [False, False, False, False, False, False, False, False,
               False, False, False, False, False, False, False, False]
'''small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small,
                      white_rook_small, white_bishop_small]'''
black_images = [Black_Pawn,Black_Pawn, Black_Queen, Black_King, Black_Knight, Black_Rook, Black_Bishop]
'''small_black_images = [Black_pawn_small, black_queen_small, black_king_small, black_knight_small,
                      black_rook_small, black_bishop_small]'''
black_promotions = ['Bishop', 'Knight', 'Rook', 'Queen']
black_moved = [False, False, False, False, False, False, False, False,
               False, False, False, False, False, False, False, False]
piece_list = ['Pawn', 'Queen', 'King', 'Knight', 'Rook', 'Bishop']
# check variables/ flashing counter
counter = 0
winner = ''
game_over = False
white_ep = (100, 100)
black_ep = (100, 100)
white_promote = False
black_promote = False
promo_index = 100
check = False
castling_moves = []



white_pieces = ['White_rook', 'White_knight', 'White_bishop', 'White_king', 'White_queen', 'White_bishop', 'White_knight', 'White_rook',
                'White_pawn', 'White_pawn', 'White_pawn', 'White_pawn', 'White_pawn', 'White_pawn', 'White_pawn', 'White_pawn']
white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]

Black_pieces = ['Black_rook', 'Black_knight', 'Black_bishop', 'Black_king', 'Black_queen', 'Black_bishop', 'Black_knight', 'Black_rook',
                'Black_pawn', 'Black_pawn', 'Black_pawn', 'Black_pawn', 'Black_pawn', 'Black_pawn', 'Black_pawn', 'Black_pawn']
Black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]

# Créer une liste combinée pour les pièces blanches et leurs emplacements

"""
pieces = {
    (0, 0): White_Rook, (0, 1): White_Knight, (0, 2): White_Bishop, (0, 3): White_Queen,
    (0, 4): White_King, (0, 5): White_Bishop, (0, 6): White_Knight, (0, 7): White_Rook,
    (1, 0): White_Pawn, (1, 1): White_Pawn, (1, 2): White_Pawn, (1, 3): White_Pawn,
    (1, 4): White_Pawn, (1, 5): White_Pawn, (1, 6): White_Pawn, (1, 7): White_Pawn,
    # Les positions des pièces blanches sont définies ci-dessus
    # Vous pouvez ajouter des positions pour les pièces noires ci-dessous
    (6, 0): Black_Pawn, (6, 1): Black_Pawn, (6, 2): Black_Pawn, (6, 3): Black_Pawn,
    (6, 4): Black_Pawn, (6, 5): Black_Pawn, (6, 6): Black_Pawn, (6, 7): Black_Pawn,
    (7, 0): Black_Rook, (7, 1): Black_Knight, (7, 2): Black_Bishop, (7, 3): Black_Queen,
    (7, 4): Black_King, (7, 5): Black_Bishop, (7, 6): Black_Knight, (7, 7): Black_Rook,
}
"""
pieces = {
    (0, 0): (White_Rook, "Rook", "White"), (0, 1): (White_Knight, "Knight", "White"),
    (0, 2): (White_Bishop, "Bishop", "White"), (0, 3): (White_Queen, "Queen", "White"),
    (0, 4): (White_King, "King", "White"), (0, 5): (White_Bishop, "Bishop", "White"),
    (0, 6): (White_Knight, "Knight", "White"), (0, 7): (White_Rook, "Rook", "White"),
    (1, 0): (White_Pawn, "Pawn", "White"), (1, 1): (White_Pawn, "Pawn", "White"),
    (1, 2): (White_Pawn, "Pawn", "White"), (1, 3): (White_Pawn, "Pawn", "White"),
    (1, 4): (White_Pawn, "Pawn", "White"), (1, 5): (White_Pawn, "Pawn", "White"),
    (1, 6): (White_Pawn, "Pawn", "White"), (1, 7): (White_Pawn, "Pawn", "White"),
    (6, 0): (Black_Pawn, "Pawn", "Black"), (6, 1): (Black_Pawn, "Pawn", "Black"),
    (6, 2): (Black_Pawn, "Pawn", "Black"), (6, 3): (Black_Pawn, "Pawn", "Black"),
    (6, 4): (Black_Pawn, "Pawn", "Black"), (6, 5): (Black_Pawn, "Pawn", "Black"),
    (6, 6): (Black_Pawn, "Pawn", "Black"), (6, 7): (Black_Pawn, "Pawn", "Black"),
    (7, 0): (Black_Rook, "Rook", "Black"), (7, 1): (Black_Knight, "Knight", "Black"),
    (7, 2): (Black_Bishop, "Bishop", "Black"), (7, 3): (Black_Queen, "Queen", "Black"),
    (7, 4): (Black_King, "King", "Black"), (7, 5): (Black_Bishop, "Bishop", "Black"),
    (7, 6): (Black_Knight, "Knight", "Black"), (7, 7): (Black_Rook, "Rook", "Black"),
}


captured_white_pieces= []
captured_black_pieces = []
# 0 - whites turn no selection: 1-whites turn piece selected: 2- black turn no selection, 3 - black turn piece selected
turn_step = 0
selection = 100
valid_moves = []






