import pygame

from Chess_game.constants import *
from abc import ABC, abstractmethod

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




#---------------------------------------------------------------



# Initialisation de Pygame
pygame.init()



SCREEN = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Nel's chessboard")


def draw_pieces_on_board():
    global selected_piece  # Cela n'est nécessaire que si vous modifiez selected_piece dans cette fonction

    for row in range(Rows):
        for col in range(Cols):
            # Vérifie si la case courante est celle de la pièce sélectionnée
            if selected_piece and (row, col) == selected_piece:
                highlight_color = (255, 255, 0)  # Jaune
                pygame.draw.rect(SCREEN, highlight_color, (col*Square, row*Square, Square, Square))
            else:
                # Dessine la case du plateau avec sa couleur normale
                color = White if (row + col) % 2 == 0 else blue
                pygame.draw.rect(SCREEN, color, (col*Square, row*Square, Square, Square))

            # Dessine la pièce s'il y en a une à cette position
            piece_info = pieces.get((row, col))
            if piece_info:
                piece_surface = piece_info[0]  # Suppose que piece_info[0] est une surface Pygame pour la pièce
                SCREEN.blit(piece_surface, (col*Square, row*Square))


"""
def main():
    running = True
    selected_piece = None
    possible_moves = []
    selected_position = None  # Pour stocker la position initiale de la pièce sélectionnée

    while running:
        for event in pygame.event.get():
            if event.type== pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = pos[1]//Square, pos[0]//Square
                print(row, col)
                position = (row, col)
                piece = pieces.get(position, None)
                print("Pièce à la position", position, ":", piece)

                if not selected_piece:
                    selected_piece = pieces.get((row, col))
                    piece_surface, piece_type, piece_color = selected_piece
                    print("couleur de la pièce :", piece_color)
                    print("Type de pièce :", piece_type)


                    selected_position = (row, col)
                    if selected_piece:
                        print("Pièce sélectionnée :", selected_piece)

                        if piece_type == "Pawn":
                                print(f"C'est un pion {piece_color.lower()}")
                                # Instancier un objet de la classe Pawn avec la couleur dynamique
                                pawn = Pawn(row, col, piece_color)
                                possible_moves = pawn.get_possible_moves(pieces)
                                print("Mouvements possibles du pion :", possible_moves)

                else:
                    if position in possible_moves:
                        # Supprimer la pièce de sa position initiale
                        del pieces[selected_position]
                        # Mettre à jour la piece a sa nouvelle position
                        pieces[position] = selected_piece
                        print("Pièce déplacée de", selected_position, "à", position)

                    else:
                        print("Mouvement invalide")
                    selected_piece = None
                    selected_position = None
                    possible_moves = []

            if event.type == pygame.QUIT:
                running = False
    
        SCREEN.fill(Black)
        draw_pieces_on_board()
        pygame.display.flip()

    pygame.quit()
"""
"""
def main():
    running = True
    selected_piece = None
    possible_moves = []
    selected_position = None  # Pour stocker la position initiale de la pièce sélectionnée

    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = pos[1] // Square, pos[0] // Square
                print(row, col)
                position = (row, col)
                piece = pieces.get(position, None)
                print("Pièce à la position", position, ":", piece)

                if not selected_piece:
                    selected_piece_info = pieces.get((row, col))
                    if selected_piece_info:  # Ajoutez cette vérification ici
                        _, piece_type, piece_color = selected_piece_info
                        print("couleur de la pièce :", piece_color)
                        print("Type de pièce :", piece_type)

                        selected_position = (row, col)
                        print("Pièce sélectionnée :", selected_piece_info)

                        if piece_type == "Pawn":
                            print(f"C'est un pion {piece_color.lower()}")
                            # Instancier un objet de la classe Pawn avec la couleur dynamique
                            pawn = Pawn(row, col, piece_color)
                            possible_moves = pawn.get_possible_moves(pieces)
                            print("Mouvements possibles du pion :", possible_moves)
                        # Mémoriser l'information de la pièce sélectionnée pour la suite
                        selected_piece = selected_piece_info

                else:
                    if position in possible_moves:
                        # Supprimer la pièce de sa position initiale
                        del pieces[selected_position]
                        # Mettre à jour la pièce à sa nouvelle position
                        pieces[position] = selected_piece
                        print("Pièce déplacée de", selected_position, "à", position)

                    else:
                        print("Mouvement invalide")
                    # Réinitialisation pour la prochaine action
                    selected_piece = None
                    selected_position = None
                    possible_moves = []

            if event.type == pygame.QUIT:
                running = False

        SCREEN.fill(Black)
        draw_pieces_on_board()
        pygame.display.flip()

    pygame.quit()
"""

# Assurez-vous que selected_piece est déclarée comme variable globale au début de votre script
selected_piece = None

def main():
    global selected_piece  # Ajoute cette ligne pour permettre la modification de la variable globale
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
                    if selected_piece_info:
                        _, piece_type, piece_color = selected_piece_info
                        print(f"Couleur de la pièce: {piece_color}, Type de pièce: {piece_type}")
                        selected_position = position
                        selected_piece = position  # Ici, vous mettez à jour la position sélectionnée

                        if piece_type == "Pawn":
                            print(f"C'est un pion {piece_color.lower()}")
                            pawn = Pawn(row, col, piece_color)
                            possible_moves = pawn.get_possible_moves(pieces)
                            print("Mouvements possibles du pion:", possible_moves)

                elif position == selected_piece:
                    # Clique à nouveau sur la pièce sélectionnée pour désélectionner
                    selected_piece = None
                    possible_moves = []

                elif position in possible_moves:
                    # Effectuer le mouvement
                    pieces.pop(selected_position)
                    pieces[position] = selected_piece_info
                    print(f"Pièce déplacée de {selected_position} à {position}")
                    selected_piece = None
                    possible_moves = []

                else:
                    print("Mouvement invalide")
                    # Option pour désélectionner la pièce actuellement sélectionnée
                    selected_piece = None
                    possible_moves = []

            if event.type == pygame.QUIT:
                running = False

        SCREEN.fill(Black)
        draw_pieces_on_board()  # S'assurer que cette fonction gère `selected_piece` pour mettre en évidence
        pygame.display.flip()

    pygame.quit()


main()

