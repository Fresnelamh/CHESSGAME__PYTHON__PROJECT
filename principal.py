import pygame
import json
from Chess_game.constants import *
from abc import ABC, abstractmethod



#----------------------Classes des pièces----------------------#
joueur_actuel="Black"

class Piece:
    def __init__(self,row,col,color, name):
        self.color = color 
        self.name = name
        self.row = row
        self.col = col

  
    @abstractmethod
    def get_possible_moves():
        pass

class Pawn(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color, "Pawn")
        self.first_move = True  

    def get_possible_moves(self, pieces):
        
        moves = []
        if self.color == "Black":
            direction = -1
            starting_row = 6
        else:
            direction = 1
            starting_row = 1

       
        one_step_forward = self.row + direction
        mouvement = (one_step_forward, self.col)
        piece = pieces.get(mouvement, None)
        if 0 <= one_step_forward < 8 and piece is None:
            moves.append(mouvement)
            if self.row == starting_row:
               
                two_steps_forward = self.row + 2 * direction
                mouvement = (two_steps_forward, self.col)
                piece = pieces.get(mouvement, None)
                if 0 <= two_steps_forward < 8 and piece is None:
                    moves.append(mouvement)

        # Captures diagonales
        for col_diagonal in [-1, 1]:
            c_row = self.row + direction
            c_col = self.col + col_diagonal
            if 0 <= c_row < 8 and 0 <= c_col < 8:
                piece = pieces.get((c_row, c_col), None)
                if piece is not None and piece[2] != self.color:
                    moves.append((c_row, c_col))

        return moves















class King(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color, "King")

    def get_possible_moves(self, pieces):
        moves = []
        # Définit tous les mouvements possibles pour le roi
        movement = [
            (0, 1),   
            (1, 1),   
            (1, 0),   
            (1, -1),  
            (0, -1),  
            (-1, -1), 
            (-1, 0),  
            (-1, 1),  
        ]

       
        
        for move in movement:
            new_row, new_col = self.row + move[0], self.col + move[1]

            # Vérifie que la nouvelle position est dans les limites de l'échiquier
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                # Obtient l'information sur la pièce à la nouvelle position
                piece = pieces.get((new_row, new_col), None)

                # Vérifie que la case cible est vide ou occupée par une pièce adverse
                if piece is None or piece[2] != self.color:
                    moves.append((new_row, new_col))

        return moves

class Rook(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color, "Rook")

    def get_possible_moves(self, pieces):
        moves = []
        directions = [
            (1, 0),
            (-1, 0), 
            (0, 1),  
            (0, -1)  
        ]

       
        for r, c in directions:
            for i in range(1, 8): 
                new_row = self.row + r * i
                new_col = self.col + c * i

               
                if not (0 <= new_row < 8 and 0 <= new_col < 8):
                    break 

                piece = pieces.get((new_row, new_col), None)

                # Vérifier la case cible
                if piece:
                 
                    if piece[2] != self.color:
                        moves.append((new_row, new_col))  
                    break 
                else:
                    moves.append((new_row, new_col)) 

        return moves

class Knight(Piece):

    def __init__(self, row, col, color):
        super().__init__(row, col, color, "King")
    
    def get_possible_moves(self, pieces):
        moves = []
      
      
        movement = [
            (1, -2),
            (2, -1),
            (2, 1),
            (1, 2),
            (-1, 2),
            (-2, 1),
            (-2, -1),
            (-1, -2)
        ]


        for move in movement:
            new_pos = (self.row + move[0], self.col + move[1])
            if (
                new_pos[0] < 8 and
                new_pos[0] >= 0 and 
                new_pos[1] < 8 and 
                new_pos[1] >= 0
            ):
                piece = pieces.get((new_pos[0], new_pos[1]), None)

              
                if piece is None or piece[2] != self.color:
                    
                   moves.append((new_pos))
        return moves


class Bishop(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color, "Bishop")

    def get_possible_moves(self, pieces):
        moves = []
      
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

      
        for r, c in directions:
            for distance in range(1, 8): 
                new_row, new_col = self.row + r * distance, self.col + c * distance

                
                if not (0 <= new_row < 8 and 0 <= new_col < 8):
                    break 

                piece = pieces.get((new_row, new_col), None)

            
                if piece:
                    # Si une pièce est présente, vérifier sa couleur
                    if piece[2] != self.color:
                        moves.append((new_row, new_col))  # Capturer la pièce adverse
                    break  
                else:
                    moves.append((new_row, new_col))  # Ajouter la position si elle est vide

        return moves


 

class Queen(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color, "Queen")

    def get_possible_moves(self, pieces):
        moves = []
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1), 
            (1, 1), (1, -1), (-1, 1), (-1, -1) 
        ]

       
        for r, c in directions:
            for i in range(1, 8): 
                new_row, new_col = self.row + r * i, self.col + c * i
                if not (0 <= new_row < 8 and 0 <= new_col < 8):
                    break 

                piece = pieces.get((new_row, new_col), None)
                if piece:
                    if piece[2] != self.color:
                        moves.append((new_row, new_col))  
                    break  
                moves.append((new_row, new_col)) 

        return moves














#---------------------------------------------------------------



# Initialisation de Pygame
pygame.init()



SCREEN = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Nel's chessboard")


selected_piece = None
def draw_pieces_on_board():
  
    selected_piece  

    for row in range(Rows):
        for col in range(Cols):
          
            if selected_piece and (row, col) == selected_piece:
                highlight_color = (255, 255, 0)  # Jaune
                pygame.draw.rect(SCREEN, highlight_color, (col*Square, row*Square, Square, Square))
            else:
              
                color = White if (row + col) % 2 == 0 else blue
                pygame.draw.rect(SCREEN, color, (col*Square, row*Square, Square, Square))

          
            piece_info = pieces.get((row, col))
            if piece_info:
                piece_surface = piece_info[0]  
                SCREEN.blit(piece_surface, (col*Square, row*Square))





        joueur_actuel=="Black"
def change_player():
    global joueur_actuel
     
    if joueur_actuel == "Black":
        joueur_actuel = "White"
    else:
        joueur_actuel = "Black"  


def main():
    global joueur_actuel
    global selected_piece
    running = True
    possible_moves = []
    selected_position = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = pos[1] // Square, pos[0] // Square
                position = (row, col)

                if not selected_piece:
                    selected_piece_info = pieces.get(position)
                    if selected_piece_info and selected_piece_info[2] == joueur_actuel:
                        _, piece_type, piece_color = selected_piece_info
                        print(f"{joueur_actuel} a sélectionné une pièce {piece_type} à {position}.")
                        selected_position = position
                        selected_piece = position 

                        # Générez les mouvements possibles selon le type de la pièce
                        if piece_type == "Pawn":
                            pawn = Pawn(row, col, piece_color)
                            possible_moves = pawn.get_possible_moves(pieces)
                        elif piece_type == "Rook":
                            rook = Rook(row, col, piece_color)
                            possible_moves = rook.get_possible_moves(pieces)
                        elif piece_type == "King":
                            king = King(row, col, piece_color)
                            possible_moves = king.get_possible_moves(pieces)
                        elif piece_type == "Knight":
                            knight = Knight(row, col, piece_color)
                            possible_moves = knight.get_possible_moves(pieces)
                        elif piece_type == "Bishop":
                            bishop = Bishop(row, col, piece_color)
                            possible_moves = bishop.get_possible_moves(pieces)
                        elif piece_type == "Queen":
                            queen = Queen(row, col, piece_color)
                            possible_moves = queen.get_possible_moves(pieces)

                        print(f"Mouvements possibles : {possible_moves}")
                    else:
                        print("Ce n'est pas le tour de cette pièce ou la pièce n'existe pas.")

                elif position == selected_piece:
                    selected_piece = None  # Désélection de la pièce
                    possible_moves = []

                elif position in possible_moves:
                    # Effectuer le mouvement
                    pieces.pop(selected_position)
                    pieces[position] = selected_piece_info
                    print(f"Pièce déplacée de {selected_position} à {position}. Tour de {joueur_actuel} terminé.")
                    selected_piece = None
                    possible_moves = []
                    change_player()  # Changer le joueur après le mouvement valide

                else:
                    print("Mouvement invalide.")
                    selected_piece = None
                    possible_moves = []

            if event.type == pygame.QUIT:
                running = False

        SCREEN.fill(Black)
        draw_pieces_on_board()
        pygame.display.flip()

  










