from abc import ABC, abstractmethod
from Chess_game.constants import *

#----------------------Classes des pièces----------------------#


class Piece:
    def __init__(self,row,col,color, name):
        self.color = color  # "White" ou "Black"
        self.name = name
        self.row = row
        self.col = col

    def move(self, board, start_pos, end_pos):
        # Logique générique de mouvement (à personnaliser dans les sous-classes)
        pass
    # Méthode pour obtenir les mouvements possibles pour une pièce
    @abstractmethod
    def get_possible_moves():
        pass



class Pawn(Piece):
    def __init__(self,row,col,color):
        super().__init__(row,col,color,"Pawn")
        self.first_move = True  # Ce booléen est utilisé pour vérifier si le pion n'a pas encore bougé

    def get_possible_moves(self, board):
        """
        Determine les mouvements possibles pour un pion pawn 
        """
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
        #print("Pièce à la position dans pawn black", mouvement, ":", piece)

        if 0 <= one_step_forward < 8 and piece is None:
            moves.append(mouvement)
            if self.row == starting_row:
                two_steps_forward = self.row + 2 * direction

                mouvement = (two_steps_forward, self.col)
                piece = pieces.get(mouvement, None)
                if 0 <= two_steps_forward < 8 and piece is None:
                    moves.append(mouvement)

        # Vérifiez les captures diagonales
        #A faire            

        return moves
