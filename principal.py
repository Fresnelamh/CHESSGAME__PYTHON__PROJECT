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
    
'''class Rook(Piece):
   def __init__(self,row,col,color):
        super().__init__(row,col,color,"Rook")
    

   def get_possible_moves(self, board):
        """
        Determine les mouvements possibles pour un pion pawn 
        """
        moves = []
        
        if self.color==Black and self.row==7 and self.col==0:
            for i in range(0,8):
                direction1=-i
                direction2=+1
        elif self.color==Black and self.row==7 and self.col==7:
             for i in range(0,8):
                 direction1=-i
                 direction2=-i
        elif self.color==White and self.row==0 and self.col==0:
           for i in range (0,8):
                 direction1=+i
                 direction2=+i
        elif self.color==White and self.row==0 and self.col==7:
            for i in range (0,8):
                direction1=+i
                direction2=-i
        
        step_forward=self.row+direction1
        step_right_left=self.col+direction2

        mouvement1=(step_forward,self.col)
        mouvement2=(self.row,step_right_left)
       
        piece1= pieces.get(mouvement1,None)
        piece2=pieces.get(mouvement2,None)


        if 0 <= step_forward < 8 and piece1 is None:
            moves.append(mouvement1)
        if 0 <= step_right_left < 8 and piece2 is None:
             moves.append(mouvement2)
            
        return moves '''
    

'''class Rook(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color, "Rook")

    def get_possible_moves(self, board):
        output = []
        moves_north = []
        for y in range(self.row - 1, -1, -1):
            piece = board.get((y, self.col))
            if piece is None:
                moves_north.append((y, self.col))
            else:
                if piece.color != self.color:
                    moves_north.append((y, self.col))
                break
        output.append(moves_north)

        moves_east = []
        for x in range(self.col + 1, 8):
            piece = board.get((self.row, x))
            if piece is None:
                moves_east.append((self.row, x))
            else:
                if piece.color != self.color:
                    moves_east.append((self.row, x))
                break
        output.append(moves_east)

        moves_south = []
        for y in range(self.row + 1, 8):
            piece = board.get((y, self.col))
            if piece is None:
                moves_south.append((y, self.col))
            else:
                if piece.color != self.color:
                    moves_south.append((y, self.col))
                break
        output.append(moves_south)

        moves_west = []
        for x in range(self.col - 1, -1, -1):
            piece = board.get((self.row, x))
            if piece is None:
                moves_west.append((self.row, x))
            else:
                if piece.color != self.color:
                    moves_west.append((self.row, x))
                break
        output.append(moves_west)

        return output
'''







class King(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color, "King")
    
    def get_possible_moves(self, board):
        moves = []
        '''movement = [
            (0,-1), # north
            (1, -1), # ne
            (1, 0), # east
            (1, 1), # se
            (0, 1), # south
            (-1, 1), # sw
            (-1, 0), # west
            (-1, -1), # nw'''
        
        # Définition des directions de mouvement pour le roi blanc (ligne 0)
        if self.color =="White":
           movement = [
            (0, 1),   # south
            (1, 1),   # se
            (1, 0),   # east
            (1, -1),  # ne
            (0, -1),  # north
             # nw
            (-1, 0),  # west
            (-1, 1),  # sw
                ]

# Définition des directions de mouvement pour le roi noir (ligne 7)
        elif self.color == "Black":
                 movement = [
           (0, -1),  # north
           (-1, -1), # nw
           (-1, 0),  # west
           (-1, 1),  # sw
           (0, 1),   # south
              # se
              (1, 0),   # east
             (1, -1),  # ne
                 ]

        for move in movement:
            new_pos = (self.row + move[0], self.col + move[1])
            if (
                new_pos[0] < 8 and
                new_pos[0] >= 0 and 
                new_pos[1] < 8 and 
                new_pos[1] >= 0
            ):
                if (new_pos[0], new_pos[1]) != (self.row, self.col):
                    moves.append(
                  
                        new_pos
                    )
                
        return moves

class Rook(Piece):
   def __init__(self, row, col, color):
        super().__init__(row, col, color, "Rook")
    
   def get_possible_moves(self, board):
        moves = []
       
    #if self.color == "Black":
        
        movement = [
          (6, 0),  # Déplacement d'une case vers le nord
         (5, 0),  # Déplacement d'une case vers le nord
        (4, 0),  # Déplacement d'une case vers le nord
        (3, 0),  # Déplacement d'une case vers le nord
         (2, 0),  # Déplacement d'une case vers le nord
         (1, 0),  # Déplacement d'une case vers le nord
         (0, 0),  # Déplacement d'une case vers le nord (arrêt à la limite du plateau)
         (7, 1),  # Déplacement d'une case vers l'ouest
           (7, 2),  # Déplacement d'une case vers l'ouest
          (7, 3),  # Déplacement d'une case vers l'ouest
           (7, 4),  # Déplacement d'une case vers l'ouest
            (7, 5),  # Déplacement d'une case vers l'ouest
            (7, 6),  # Déplacement d'une case vers l'ouest
               (7, 7),  # Déplacement d'une case vers l'ouest (arrêt à la limite du plateau)
            ]

       
        for move in movement:
            new_row, new_col = move[0], move[1]
            # Vérifier si le mouvement est à l'intérieur du plateau
            if 0 <= new_row < self.row<8 and 0 <= new_col <= self.col<8:
           
                piece_color = pieces.get((new_row, new_col),None)  # Récupérer la couleur de la pièce à la nouvelle position
                if (new_row, new_col) != (self.row, self.col) and (piece_color is None or piece_color != self.color):
                    moves.append((new_row, new_col))
                elif piece_color==self.color:
                    break

        return moves

class Knight(Piece):

    def __init__(self, row, col, color):
        super().__init__(row, col, color, "King")
    
    def get_possible_moves(self, board):
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
                moves.append(
                    (
                        new_pos
                    )
                )
        return moves

class Bishop(Piece):

  def __init__(self, row, col, color):
        super().__init__(row, col, color, "Bishop")
 




  def get_possible_moves(self, board):
        moves = []
     
        for i in range(1, 8):
            if self.row + i > 7 or self.col - i < 0:
                break
          
            movement=(self.row + i, self.col - i)
            moves.append(movement)
    
        for i in range(1, 8):
            if self.row + i > 7 or self.col + i > 7:
                break
            
            
            movement=(self.row + i, self.col + i)
            moves.append(movement)
       
        for i in range(1, 8):
            if self.row - i < 0 or self.col + i > 7:
                break
            
            
            movement= (self.row - i, self.col + i)
            moves.append(movement)
      
        for i in range(1, 8):
            if self.row - i < 0 or self.col - i < 0:
                break
          
           
            movement=(self.row - i, self.col - i)
        
            moves.append(movement)
              
      
        return moves

class Queen(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color, "Queen")
 


    def get_possible_moves(self, pieces):
        moves = []
        
        # Vertical and horizontal movements
        for row in range(self.row - 1, -1, -1):
            moves.append((row, self.col))
            if pieces.get((row, self.col), None) is not None:
                break
        
        for row in range(self.row + 1, 8):
            moves.append((row, self.col))
            if pieces.get((row, self.col), None) is not None:
                break
        
        for col in range(self.col - 1, -1, -1):
            moves.append((self.row, col))
            if pieces.get((self.row, col), None) is not None:
                break
        
        for col in range(self.col + 1, 8):
            moves.append((self.row, col))
            if pieces.get((self.row, col), None) is not None:
                break
        
        # Diagonal movements
        for i in range(1, 8):
            if self.row - i < 0 or self.col - i < 0:
                break
            moves.append((self.row - i, self.col - i))
            if pieces.get((self.row - i, self.col - i), None) is not None:
                break
        
        for i in range(1, 8):
            if self.row - i < 0 or self.col + i > 7:
                break
            moves.append((self.row - i, self.col + i))
            if pieces.get((self.row - i, self.col + i), None) is not None:
                break
        
        for i in range(1, 8):
            if self.row + i > 7 or self.col - i < 0:
                break
            moves.append((self.row + i, self.col - i))
            if pieces.get((self.row + i, self.col - i), None) is not None:
                break
        
        for i in range(1, 8):
            if self.row + i > 7 or self.col + i > 7:
                break
            moves.append((self.row + i, self.col + i))
            if pieces.get((self.row + i, self.col + i), None) is not None:
                break
        
        return moves

 















#---------------------------------------------------------------



# Initialisation de Pygame
pygame.init()



SCREEN = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Nel's chessboard")


'''def'' changer_joueur():
    global current_player
    current_player = "Black" if current_player == "White" else "White"'''

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
                        elif piece_type=="Rook":
                            print(f"C'est une tour {piece_color.lower()}")
                            rook=Rook(row,col,piece_color)
                            possible_moves=rook.get_possible_moves(pieces)
                        elif piece_type == "King":
                            print(f"C'est un roi {piece_color.lower()}")
                            roi= King(row, col, piece_color)
                            possible_moves = roi.get_possible_moves(pieces)
                            print("Mouvements possibles du roi :", possible_moves)
                        elif piece_type=="Knight":
                            print(f"C'est un cavalier {piece_color.lower()}")
                            knight= Knight(row, col, piece_color)
                            possible_moves = knight.get_possible_moves(pieces)
                            print("Mouvements possibles du roi :", possible_moves)
                        elif piece_type=="Bishop":
                            print(f"C'est un fou {piece_color.lower()}")
                            bishop= Bishop(row, col, piece_color)
                            possible_moves = bishop.get_possible_moves(pieces)
                            print("Mouvements possibles d'un fou :", possible_moves)
                        elif piece_type=="Queen":
                            print(f"C'est une reine {piece_color.lower()}")
                            queen= Queen(row, col, piece_color)
                            possible_moves = queen.get_possible_moves(pieces)
                            print("Mouvements possibles d'une reine  :", possible_moves)
                        
                     
                     
   
                           


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

 
























'''import pygame

from Chess_game.constants import *
from abc import ABC, abstractmethod

#----------------------Classes des pièces----------------------#
current_player="White"

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


def changer_joueur():
    global current_player
    current_player = "Black" if current_player == "White" else "White"

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


main()'''

 

