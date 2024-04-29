



import pygame
import os

Width=605

Height=605

Rows=8

Cols=8



Square=Width//Rows

#couleurs des cases du tableau
brown=(87,16,16)
Black = (0, 0, 0)
White=(255,255,255)
blue=(0, 0, 139)
red=(139, 0, 0, 0.342)




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








