from abc import ABC, abstractmethod
from Chess_game.constants import *

#----------------classess----------------

class Pieces_matter:
    def __init__(self, r, c, color):
        self.r = r
        self.c = c
        self.color = color
        self.position = (self.r, self.c)
        self.valid_moves = []

    @abstractmethod
    def possible_moves(self, pieces):  
        pass

    @abstractmethod 
    def echecetmat(self):  
        pass
    
    @abstractmethod 
    def pat(self): 
        pass

    def moves(self):
        self.valid_moves = []
    
    def clear_moves(self):
        if len(self.valid_moves) > 0:
            self.valid_moves = []
    def move_with_mouse(self, new_r, new_c):
        # Déplace la pièce aux coordonnées spécifiées par la souris
        self.r = new_r
        self.c = new_c
        self.position = (self.r, self.c)

    def handle_mouse_event(self, event):
        # Gère les événements de la souris pour déplacer la pièce
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            new_c = mouse_pos[0] // Square
            new_r = mouse_pos[1] // Square
            if (new_r, new_c) in self.valid_moves:
                self.move_with_mouse(new_r, new_c)



class BBlack(Pieces_matter):
    def __init__(self, r, c, color):
        super().__init__(r, c, color)
        self.captured_white_pieces = []  # Initialisation de la liste des pièces blanches capturées
    
    def capture_piece(self, p):
        if p.color == "White":  # Correction de la condition
            self.captured_white_pieces.append(p)
    
    def echecetmat(self, pieces):
        black_king = None
        self.captured_white_pieces = []

        # Trouver la position du roi noir
        for row in pieces:
            for piece in row:
                if isinstance(piece, King) and piece.color == "Black":
                    black_king = piece
                    break
            if black_king:
                break

        # Collecter toutes les pièces blanches
        for row in pieces:
            for piece in row:
                if piece.color == "White":
                    self.capture_piece(piece)

        # Vérifier si le roi noir est en échec
        for white_piece in self.captured_white_pieces:
            if black_king.position in white_piece.possible_moves(pieces):
                print("Le roi noir est en échec.")
                return False  # Le roi noir n'est pas en échec et mat

        # Vérifier si le roi noir est en échec et mat
        for black_piece in pieces:
            for piece in black_piece:
                if piece and piece.color == "Black":
                    moves = piece.possible_moves(pieces)
                    for move in moves:
                        new_pieces = [row[:] for row in pieces]  # Créer une copie des pièces
                        new_pieces[piece.r][piece.c], new_pieces[move[0]][move[1]] = 0, piece
                        # Vérifier si le roi noir est toujours en échec après le mouvement
                        if self.echecetmat(new_pieces):
                            return False  # Le roi noir n'est pas en échec et mat
        print("Le roi noir est en échec et mat.")
        return True  # Le roi noir est en échec et mat

    def pat(self, pieces):
         
         black_king = None
         black_pieces = []

        # Trouver la position du roi noir
         for row in pieces:
            for piece in row:
                if isinstance(piece, King) and piece.color == "Black":
                    black_king = piece
                    break
            if black_king:
                break

        # Collecter toutes les pièces noires
         for row in pieces:
            for piece in row:
                if piece and piece.color == "Black":
                    black_pieces.append(piece)

        # Vérifier si le roi noir a des mouvements possibles
         for black_piece in black_pieces:
            moves = black_piece.possible_moves(pieces)
            if moves:
                return False  # Il y a des mouvements possibles pour les pièces noires, donc pas de pat

        # Vérifier si le roi noir est en échec
         for black_piece in black_pieces:
            if black_king.position in black_piece.possible_moves(pieces):
                return False  # Le roi noir est en échec, donc pas de pat

         print("Pat !")
         return True  # Pat est atteint

    
    

class BPawn(BBlack):
    def __init__(self, r, c, color):
        super().__init__(r, c, color)
        self.first_move = True

    def possible_moves(self):
        #self.clear_moves()
        
        if self.color == Black:
            if self.r - 1 >= 0:
                if pieces[self.r - 1][self.c] == 0: 
                    self.valid_moves.append((self.r - 1, self.c))

                if self.first_move:
                    if pieces[self.r - 1][self.c] == 0 and pieces[self.r - 2][self.c] == 0:
                        self.valid_moves.append((self.r - 2, self.c))

                if self.c - 1 >= 0:
                    if pieces[self.r - 1][self.c - 1] != 0:
                        piece = pieces[self.r - 1][self.c - 1]
                        if piece.color != Black:
                            self.capture_piece(pieces[self.r - 1][self.c - 1])
                            self.valid_moves.append((self.r - 1, self.c - 1))

                if self.c + 1 < len(pieces[0]):
                    if pieces[self.r - 1][self.c + 1] != 0:
                        piece = pieces[self.r - 1][self.c + 1]
                        if piece.color != Black:
                            self.capture_piece(pieces[self.r - 1][self.c + 1])
                            self.valid_moves.append((self.r - 1, self.c + 1))

        return self.valid_moves
    
class Rook(BBlack):
    def __init__(self, r, c, color):
        super().__init__(r, c, color)
      
    def possible_moves(self, pieces):
        self.clear_moves()
        # Coups verticaux des tours
        for i in range(self.r + 1, 8):
            if pieces[i][self.c] == 0:
                self.valid_moves.append((i, self.c))
            else:  # Si la case n'est pas vide
                if pieces[i][self.c].color != Black:
                    self.capture_piece(pieces[i][self.c])
                    self.valid_moves.append((i, self.c))
                    break  # S'arrêter après avoir mangé la pièce
                else:
                    break  # Si c'est une autre couleur de pièce, s'arrêter automatiquement

        for j in range(self.r - 1, -1, -1):  # Déplacer la tour sur la ligne précédente pas -1 et fin -1 en commençant par la ligne d'indice row-1
            if pieces[j][self.c] == 0:
                self.valid_moves.append((j, self.c))
            else:  # Si la case n'est pas vide
                if pieces[j][self.c].color != Black:
                    self.capture_piece(pieces[j][self.c])
                    self.valid_moves.append((j, self.c))
                    break  # S'arrêter après avoir mangé la pièce
                else:
                    break  # Si c'est une autre couleur de pièce, s'arrêter automatiquement

   
        # Coups horizontaux des tours
        for j in range(self.c + 1, 8):
            if pieces[self.r][j] == 0:
                self.valid_moves.append((self.r, j))
            else:  # Si la case n'est pas vide
                if pieces[self.r][j].color != Black:
                    self.capture_piece(pieces[self.r][j])
                    self.valid_moves.append((self.r, j))
                    break  # S'arrêter après avoir mangé la pièce
                else:
                    break  # Si c'est une autre couleur de pièce, s'arrêter automatiquement

        for f in range(self.c - 1, -1, -1):  # Coups vers la gauche
            if pieces[self.r][f] == 0:
                self.valid_moves.append((self.r, f))
            else:  # Si la case n'est pas vide
                if pieces[self.r][f].color != Black:
                    self.capture_piece(pieces[self.r][f])
                    self.valid_moves.append((self.r, f))
                    break  # S'arrêter après avoir mangé la pièce
                else:
                    break  # Si c'est une autre couleur de pièce, s'arrêter automatiquement


        return self.valid_moves

class Bishop(BBlack):
    def __init__(self, r, c, color):
        super().__init__(r, c, color)

    def possible_moves(self, pieces):
        self.clear_moves()
        r = self.r + 1
        c = self.c + 1
        
        while r <= 7 and c <= 7:
            if pieces[r][c] == 0:
                self.valid_moves.append((r, c))
                r += 1
                c += 1
            else:
                if pieces[r][c].color != Black:
                    self.capture_piece(pieces[r][c])
                    self.valid_moves.append((r, c))
                break

        r = self.r - 1
        c = self.c - 1

        while r >= 0 and c >= 0:
            if pieces[r][c] == 0:
                self.valid_moves.append((r, c))
                r -= 1
                c -= 1
            else:
                if pieces[r][c].color != Black:
                    self.capture_piece(pieces[r][c])
                    self.valid_moves.append((r, c))
                break

        r = self.r + 1
        c = self.c - 1

        while r <= 7 and c >= 0:
            if pieces[r][c] == 0:
                self.valid_moves.append((r, c))
                r += 1
                c -= 1
            else:
                if pieces[r][c].color != Black:
                    self.capture_piece(pieces[r][c])
                    self.valid_moves.append((r, c))
                break

        r = self.r - 1
        c = self.c + 1

        while r >= 0 and c <= 7:
            if pieces[r][c] == 0:
                self.valid_moves.append((r, c))
                r -= 1
                c += 1
            else:
                if pieces[r][c].color != Black:
                    self.capture_piece(pieces[r][c])
                    self.valid_moves.append((r, c))
                break

        return self.valid_moves

class Knight(BBlack):
    def __init__(self, r, c, color):
        super().__init__(r, c, color)

    def possible_moves(self, pieces):
        self.clear_moves()   

        if self.r - 2 >= 0 and self.c + 1 <= 7:
            if pieces[self.r - 2][self.c + 1] == 0 or pieces[self.r - 2][self.c + 1].color !=Black:
                self.capture_piece(pieces[self.r - 2][self.c + 1])
                self.valid_moves.append((self.r - 2, self.c + 1))

        if self.r - 2 >= 0 and self.c - 1 >= 0:
            if pieces[self.r - 2][self.c - 1] == 0 or pieces[self.r - 2][self.c - 1].color != Black:
                self.capture_piece(pieces[self.r - 2][self.c - 1])
                self.valid_moves.append((self.r - 2, self.c - 1))

        if self.r + 2 <= 7 and self.c + 1 <= 7:
            if pieces[self.r + 2][self.c + 1] == 0 or pieces[self.r + 2][self.c + 1].color != Black:
                 self.capture_piece(pieces[self.r +2][self.c +1])
                 self.valid_moves.append((self.r + 2, self.c + 1))

        if self.r + 2 <= 7 and self.c - 1 >= 0:
            if pieces[self.r + 2][self.c - 1] == 0 or pieces[self.r + 2][self.c - 1].color != Black:
                 self.capture_piece(pieces[self.r +2][self.c - 1])
                 self.valid_moves.append((self.r + 2, self.c - 1))

        if self.r + 1 <= 7 and self.c - 2 >= 0:
            if pieces[self.r + 1][self.c - 2] == 0 or pieces[self.r + 1][self.c - 2].color != Black:
                 self.capture_piece(pieces[self.r +1][self.c - 2])
                 self.valid_moves.append((self.r + 1, self.c - 2))

        if self.r + 1 <= 7 and self.c + 2 <= 7:
            if pieces[self.r + 1][self.c + 2] == 0 or pieces[self.r + 1][self.c + 2].color != Black:
                 self.capture_piece(pieces[self.r +1][self.c +2])
                 self.valid_moves.append((self.r + 1, self.c + 2))

        if self.r - 1 >= 0 and self.c + 2 <= 7:
            if pieces[self.r - 1][self.c + 2] == 0 or pieces[self.r - 1][self.c + 2].color != Black:
                 self.capture_piece(pieces[self.r - 1][self.c +2])
                 self.valid_moves.append((self.r - 1, self.c + 2))

        if self.r - 1 >= 0 and self.c - 2 >= 0:
            if pieces[self.r - 1][self.c - 2] == 0 or pieces[self.r - 1][self.c - 2].color != Black:
                 self.capture_piece(pieces[self.r - 1][self.c - 2])
                 self.valid_moves.append((self.r - 1, self.c - 2))

        return self.valid_moves




class Queen(BBlack):


    def __init__(self, r, c, color):
        super().__init__(r, c, color)

    def possible_moves(self, pieces):
        self.clear_moves() 
        # Coups verticaux de la reine
        for i in range(self.r + 1, 8):
            if pieces[i][self.c] == 0:
                self.valid_moves.append((i, self.c))
            else:  # Si la case n'est pas vide
                if pieces[i][self.c].color != Black:
                    self.capture_piece(pieces[i][self.c])
                    self.valid_moves.append((i, self.c))
                    break  # S'arrêter après avoir mangé la pièce
                else:
                    break  # Si c'est une autre couleur de pièce, s'arrêter automatiquement

        for j in range(self.r - 1, -1, -1):  # Déplacer la tour sue la ligne précédante pas -1 et fin -1 en commençant par la ligne d'indice row-1
            if pieces[j][self.c] == 0:
                self.valid_moves.append((j, self.c))
            else:  # Si la case n'est pas vide
                self.capture_piece(pieces[j][self.c])
                if pieces[j][self.c].color != Black:
                    self.valid_moves.append((j, col))
                    break  # S'arrêter après avoir mangé la pièce
                else:
                    break  # Si c'est une autre couleur de pièce, s'arrêter automatiquement

        # Coups horizontaux de la reine
        for j in range(self.c + 1, 8):
            if pieces[self.r][j] == 0:
                self.valid_moves.append((self.r, j))
            else:  # Si la case n'est pas vide
                if pieces[self.r][j].color != Black:
                    self.capture_piece(pieces[self.r][j])
                    self.valid_moves.append((self.r, j))
                    break  # S'arrêter après avoir mangé la pièce
                else:
                    break  # Si c'est une autre couleur de pièce, s'arrêter automatiquement

        for f in range(self.c - 1, -1, -1):  # coups vers la gauche
            if pieces[f][self.c] == 0:
                self.valid_moves.append((f, self.c))
            else:  # Si la case n'est pas vide
                if pieces[f][self.c].color != Black:
                    self.capture_piece(pieces[f][self.c])
                    self.valid_moves.append((f, self.c))
                    break  # S'arrêter après avoir mangé la pièce
                else:
                    break  # Si c'est une autre couleur de pièce, s'arrêter automatiquement

        # Coups en diagonale
        r = self.r + 1
        c = self.c + 1

        while r <= 7 and c <= 7:
            if pieces[r][c] == 0:  # si la case en diagonale est libre
                self.valid_moves.append((r, c))  # se déplacer dans cette case
                r += 1
                c += 1
            else:
                if pieces[r][c].color != Black:  # Si cette case en diagonale comporte une pièce de couleur différente
                    self.capture_piece(pieces[r][c])
                    self.valid_moves.append((r, c))  # Manger la pièce
                    break  # Ensuite sortir de la boucle
                else:
                    break  # Sinon déjà s'arrêter à la position actuelle

        # Coups en diagonale
        r = self.r - 1
        c = self.c - 1

        while r >= 0 and c >= 0:  # déplacement vers la gauche tant que r et c sont positifs
            if pieces[r][c] == 0:  # si la case en diagonale est libre
                self.valid_moves.append((r, c))  # se déplacer dans cette case
                r -= 1
                c -= 1
            else:
                if pieces[r][c].color != self.color:  # Si cette case en diagonale comporte une pièce de couleur différente
                    self.capture_piece(pieces[r][c])
                    self.valid_moves.append((r, c))  # Manger la pièce
                    break  # Ensuite sortir de la boucle
                else:
                    break  # Sinon déjà s'arrêter à la position actuelle

        r = self.r + 1  # Diagonale ligne qui augmente et colonne qui diminue
        c = self.c - 1

        while r <= 7 and c >= 0:
            if pieces[r][c] == 0:  # si la case en diagonale est libre
                self.valid_moves.append((r, c))  # se déplacer dans cette case
                r += 1
                c -= 1
            else:
                if pieces[r][c].color != Black:  # Si cette case en diagonale comporte une pièce de couleur différente
                    self.capture_piece(pieces[r][c])
                    self.valid_moves.append((r, c))  # Manger la pièce
                    break  # Ensuite sortir de la boucle
                else:
                    break  # Sinon déjà s'arrêter à la position actuelle

        r = self.r - 1  # Diagonale ligne qui diminue et colonne qui augmente
        c = self.c + 1

        while r >= 0 and c <= 7:
            if pieces[r][c] == 0:  # si la case en diagonale est libre
                self.valid_moves.append((r, c))  # se déplacer dans cette case
                r -= 1
                c += 1
            else:
                if pieces[r][c].color != Black:  # Si cette case en diagonale comporte une pièce de couleur différente
                    self.capture_piece(pieces[r][c])
                    self.valid_moves.append((r, c))  # Manger la pièce
                    break  # Ensuite sortir de la boucle
                else:
                    break  # Sinon déjà s'arrêter à la position actuelle

        return self.valid_moves

class King(BBlack):  # 
       def __init__(self, r, c, color):
        super().__init__(r, c, color)

       def possible_moves(self, pieces):
        self.clear_moves() 

        # Coups Verticaux   
        if self.r - 1 >= 0 :
            if pieces[self.r - 1][self.c] == 0 or pieces[self.r - 1][self.c].color != Black:
                self.capture_piece(pieces[self.r - 1][self.c])
                self.valid_moves.append((self.r - 1, self.c))

        if self.r + 1 <= 7:
            if pieces[self.r + 1][self.c] == 0 or pieces[self.r + 1][self.c].color != Black:
                self.capture_piece(pieces[self.r + 1][self.c])
                self.valid_moves.append((self.r + 1, self.c))

        # Coups horizontaux           
        if self.c - 1 >= 0:
            if pieces[self.r][self.c - 1] == 0 or pieces[self.r][self.c - 1].color != Black:
                self.valid_moves.append((self.r, self.c - 1))

        if self.c + 1 <= 7:
            if pieces[self.r][self.c + 1] == 0 or pieces[self.r][self.c + 1].color != Black:
                self.valid_moves.append((self.r, self.c + 1))

        # Coups en diagonale
        if self.r - 1 >= 0 and self.c - 1 >= 0:
            if pieces[self.r - 1][self.c - 1] == 0 or pieces[self.r - 1][self.c - 1].color != Black:
                self.valid_moves.append((self.r - 1, self.c - 1))

        if self.r - 1 >= 0 and self.c + 1 <= 7:
            if pieces[self.r - 1][self.c + 1] == 0 or pieces[self.r - 1][self.c + 1].color != Black:
                self.valid_moves.append((self.r - 1, self.c + 1))

        if self.r + 1 <= 7 and self.c + 1 <= 7:
            if pieces[self.r + 1][self.c + 1] == 0 or pieces[self.r + 1][self.c + 1].color != Black:
                self.valid_moves.append((self.r + 1, self.c + 1))

        if self.r + 1 <= 7 and self.c - 1 >= 0:
            if pieces[self.r + 1][self.c - 1] == 0 or pieces[self.r + 1][self.c - 1].color != Black:
                self.valid_moves.append((self.r + 1, self.c - 1))

        return self.valid_moves

class WWhite(Pieces_matter):
    def __init__(self, r, c, color):
        super().__init__(r, c, color)
        self.captured_black_pieces = []  # Initialisation de la liste des pièces blanches capturées
    
    def capture_piece(self, p):
        if p.color == Black:  # Correction de la condition
            self.captured_black_pieces.append(p)
    
    def echec_et_mat(self, pieces):
        white_king = None
        captured_black_pieces = []
        
        # Trouver la position du roi blanc
        for row in pieces:
            for piece in row:
                if isinstance(piece, King) and piece.color == "White":
                    white_king = piece
                    break
            if white_king:
                break
        
        # Collecter toutes les pièces noires
        for row in pieces:
            for piece in row:
                if piece and piece.color == "Black":
                    captured_black_pieces.append(piece)
        
        # Vérifier si le roi blanc est en échec
        for black_piece in captured_black_pieces:
            if white_king.position in black_piece.possible_moves(pieces):
                print("Le roi blanc est en échec.")
                return False  # Le roi blanc n'est pas en échec et mat
        
        # Vérifier si le roi blanc est en échec et mat
        for white_piece in pieces:
            for piece in white_piece:
                if piece and piece.color == "White":
                    moves = piece.possible_moves(pieces)
                    for move in moves:
                        new_pieces = [row[:] for row in pieces]  # Créer une copie des pièces
                        new_pieces[piece.r][piece.c], new_pieces[move[0]][move[1]] = 0, piece
                        # Vérifier si le roi blanc est toujours en échec après le mouvement
                        if self.echec_et_mat(new_pieces):
                            return False  # Le roi blanc n'est pas en échec et mat
        print("Le roi blanc est en échec et mat.")
        return True  # Le roi blanc est en échec et mat
    
    def pat(self, pieces):
        white_king = None
        white_pieces = []
        
        # Trouver la position du roi blanc
        for row in pieces:
            for piece in row:
                if isinstance(piece, King) and piece.color == "White":
                    white_king = piece
                    break
            if white_king:
                break
        
        # Collecter toutes les pièces blanches
        for row in pieces:
            for piece in row:
                if piece and piece.color == "White":
                    white_pieces.append(piece)
        
        # Vérifier si le roi blanc a des mouvements possibles
        for white_piece in white_pieces:
            moves = white_piece.possible_moves(pieces)
            if moves:
                return False  # Il y a des mouvements possibles pour les pièces blanches, donc pas de pat
        
        # Vérifier si le roi blanc est en échec
        for white_piece in white_pieces:
            if white_king.position in white_piece.possible_moves(pieces):
                return False  # Le roi blanc est en échec, donc pas de pat
        
        print("Pat !")
        return True  # Pat est atteint
    


class WPawn(WWhite):
    def __init__(self, r, c, color):
        super().__init__(r, c, color)
        self.first_move = True

    def possible_moves(self, pieces):
        self.clear_moves()

        if self.color == White:
            if self.r + 1 <= 7:
                if pieces[self.r + 1][self.c] == 0:
                    self.valid_moves.append((self.r + 1, self.c))

                if self.first_move and pieces[self.r + 1][self.c] == 0 and pieces[self.r + 2][self.c] == 0:
                    self.valid_moves.append((self.r + 2, self.c))

                if self.c - 1 >= 0 and pieces[self.r + 1][self.c - 1] != 0:
                    piece = pieces[self.r + 1][self.c - 1]
                    if piece.color != White:
                        self.capture_piece(piece)
                        self.valid_moves.append((self.r + 1, self.c - 1))

                if self.c + 1 < len(pieces[0]) and pieces[self.r + 1][self.c + 1] != 0:
                    piece = pieces[self.r + 1][self.c + 1]
                    if piece.color != White:
                        self.capture_piece(piece)
                        self.valid_moves.append((self.r + 1, self.c + 1))

        return self.valid_moves

class Rook(WWhite):
    def __init__(self, r, c, color):
        super().__init__(r, c, color)
      
    def possible_moves(self, pieces):
        self.clear_moves()
        # Coups verticaux des tours
        for i in range(self.r + 1, 8):
            if pieces[i][self.c] == 0:
                self.valid_moves.append((i, self.c))
            else:  # Si la case n'est pas vide
                if pieces[i][self.c].color != White:
                    self.capture_piece(pieces[i][self.c])
                    self.valid_moves.append((i, self.c))
                    break  # S'arrêter après avoir mangé la pièce
                else:
                    break  # Si c'est une autre couleur de pièce, s'arrêter automatiquement

        for j in range(self.r - 1, -1, -1):  # Déplacer la tour sur la ligne précédente pas -1 et fin -1 en commençant par la ligne d'indice row-1
            if pieces[j][self.c] == 0:
                self.valid_moves.append((j, self.c))
            else:  # Si la case n'est pas vide
                if pieces[j][self.c].color != White:
                    self.capture_piece(pieces[j][self.c])
                    self.valid_moves.append((j, self.c))
                    break  # S'arrêter après avoir mangé la pièce
                else:
                    break  # Si c'est une autre couleur de pièce, s'arrêter automatiquement

   
        # Coups horizontaux des tours
        for j in range(self.c + 1, 8):
            if pieces[self.r][j] == 0:
                self.valid_moves.append((self.r, j))
            else:  # Si la case n'est pas vide
                if pieces[self.r][j].color != White:
                    self.capture_piece(pieces[self.r][j])
                    self.valid_moves.append((self.r, j))
                    break  # S'arrêter après avoir mangé la pièce
                else:
                    break  # Si c'est une autre couleur de pièce, s'arrêter automatiquement

        for f in range(self.c - 1, -1, -1):  # Coups vers la gauche
            if pieces[self.r][f] == 0:
                self.valid_moves.append((self.r, f))
            else:  # Si la case n'est pas vide
                if pieces[self.r][f].color != White:
                    self.capture_piece(pieces[self.r][f])
                    self.valid_moves.append((self.r, f))
                    break  # S'arrêter après avoir mangé la pièce
                else:
                    break  # Si c'est une autre couleur de pièce, s'arrêter automatiquement


        return self.valid_moves

class Bishop(WWhite):
    def __init__(self, r, c, color):
        super().__init__(r, c, color)

    def possible_moves(self, pieces):
        self.clear_moves()
        r = self.r + 1
        c = self.c + 1
        
        while r <= 7 and c <= 7:
            if pieces[r][c] == 0:
                self.valid_moves.append((r, c))
                r += 1
                c += 1
            else:
                if pieces[r][c].color != White:
                    self.capture_piece(pieces[r][c])
                    self.valid_moves.append((r, c))
                break

        r = self.r - 1
        c = self.c - 1

        while r >= 0 and c >= 0:
            if pieces[r][c] == 0:
                self.valid_moves.append((r, c))
                r -= 1
                c -= 1
            else:
                if pieces[r][c].color != White:
                    self.capture_piece(pieces[r][c])
                    self.valid_moves.append((r, c))
                break

        r = self.r + 1
        c = self.c - 1

        while r <= 7 and c >= 0:
            if pieces[r][c] == 0:
                self.valid_moves.append((r, c))
                r += 1
                c -= 1
            else:
                if pieces[r][c].color != White:
                    self.capture_piece(pieces[r][c])
                    self.valid_moves.append((r, c))
                break

        r = self.r - 1
        c = self.c + 1

        while r >= 0 and c <= 7:
            if pieces[r][c] == 0:
                self.valid_moves.append((r, c))
                r -= 1
                c += 1
            else:
                if pieces[r][c].color != White:
                    self.capture_piece(pieces[r][c])
                    self.valid_moves.append((r, c))
                break

        return self.valid_moves
    
class Knight(WWhite):
    def __init__(self, r, c, color):
        super().__init__(r, c, color)

    def possible_moves(self, pieces):
        self.clear_moves()   

        if self.r - 2 >= 0 and self.c + 1 <= 7:
            if pieces[self.r - 2][self.c + 1] == 0 or pieces[self.r - 2][self.c + 1].color != White:
                self.capture_piece(pieces[self.r - 2][self.c + 1])
                self.valid_moves.append((self.r - 2, self.c + 1))

        if self.r - 2 >= 0 and self.c - 1 >= 0:
            if pieces[self.r - 2][self.c - 1] == 0 or pieces[self.r - 2][self.c - 1].color != White:
                self.capture_piece(pieces[self.r - 2][self.c - 1])
                self.valid_moves.append((self.r - 2, self.c - 1))

        if self.r + 2 <= 7 and self.c + 1 <= 7:
            if pieces[self.r + 2][self.c + 1] == 0 or pieces[self.r + 2][self.c + 1].color != White:
                 self.capture_piece(pieces[self.r +2][self.c +1])
                 self.valid_moves.append((self.r + 2, self.c + 1))

        if self.r + 2 <= 7 and self.c - 1 >= 0:
            if pieces[self.r + 2][self.c - 1] == 0 or pieces[self.r + 2][self.c - 1].color != White:
                 self.capture_piece(pieces[self.r +2][self.c - 1])
                 self.valid_moves.append((self.r + 2, self.c - 1))

        if self.r + 1 <= 7 and self.c - 2 >= 0:
            if pieces[self.r + 1][self.c - 2] == 0 or pieces[self.r + 1][self.c - 2].color != White:
                 self.capture_piece(pieces[self.r +1][self.c - 2])
                 self.valid_moves.append((self.r + 1, self.c - 2))

        if self.r + 1 <= 7 and self.c + 2 <= 7:
            if pieces[self.r + 1][self.c + 2] == 0 or pieces[self.r + 1][self.c + 2].color != White:
                 self.capture_piece(pieces[self.r +1][self.c +2])
                 self.valid_moves.append((self.r + 1, self.c + 2))

        if self.r - 1 >= 0 and self.c + 2 <= 7:
            if pieces[self.r - 1][self.c + 2] == 0 or pieces[self.r - 1][self.c + 2].color != White:
                 self.capture_piece(pieces[self.r - 1][self.c +2])
                 self.valid_moves.append((self.r - 1, self.c + 2))

        if self.r - 1 >= 0 and self.c - 2 >= 0:
            if pieces[self.r - 1][self.c - 2] == 0 or pieces[self.r - 1][self.c - 2].color != White:
                 self.capture_piece(pieces[self.r - 1][self.c - 2])
                 self.valid_moves.append((self.r - 1, self.c - 2))

        return self.valid_moves



class Queen(WWhite):  #  Queen ou Reine est une classe fille de White
    def __init__(self, r, c, color):
        super().__init__(r, c, color)

    def possible_moves(self, pieces):
        self.clear_moves() 
        # Coups verticaux de la reine
        for i in range(self.r + 1, 8):
            if pieces[i][self.c] == 0:
                self.valid_moves.append((i, self.c))
            else:  # Si la case n'est pas vide
                if pieces[i][self.c].color != White:  # Modification ici pour vérifier si la pièce est blanche
                    self.capture_piece(pieces[i][self.c])
                    self.valid_moves.append((i, self.c))
                    break  # S'arrêter après avoir mangé la pièce
                else:
                    break  # Si c'est une autre couleur de pièce, s'arrêter automatiquement

        for j in range(self.r - 1, -1, -1):  # Déplacer la tour sue la ligne précédante pas -1 et fin -1 en commençant par la ligne d'indice row-1
            if pieces[j][self.c] == 0:
                self.valid_moves.append((j, self.c))
            else:  # Si la case n'est pas vide
                self.capture_piece(pieces[j][self.c])
                if pieces[j][self.c].color != White:  # Modification ici pour vérifier si la pièce est blanche
                    self.valid_moves.append((j, col))
                    break  # S'arrêter après avoir mangé la pièce
                else:
                    break  # Si c'est une autre couleur de pièce, s'arrêter automatiquement

        # Coups horizontaux de la reine
        for j in range(self.c + 1, 8):
            if pieces[self.r][j] == 0:
                self.valid_moves.append((self.r, j))
            else:  # Si la case n'est pas vide
                if pieces[self.r][j].color != White:  # Modification ici pour vérifier si la pièce est blanche
                    self.capture_piece(pieces[self.r][j])
                    self.valid_moves.append((self.r, j))
                    break  # S'arrêter après avoir mangé la pièce
                else:
                    break  # Si c'est une autre couleur de pièce, s'arrêter automatiquement

        for f in range(self.c - 1, -1, -1):  # coups vers la gauche
            if pieces[f][self.c] == 0:
                self.valid_moves.append((f, self.c))
            else:  # Si la case n'est pas vide
                if pieces[f][self.c].color != White:  # Modification ici pour vérifier si la pièce est blanche
                    self.capture_piece(pieces[f][self.c])
                    self.valid_moves.append((f, self.c))
                    break  # S'arrêter après avoir mangé la pièce
                else:
                    break  # Si c'est une autre couleur de pièce, s'arrêter automatiquement

        # Coups en diagonale
        r = self.r + 1
        c = self.c + 1

        while r <= 7 and c <= 7:
            if pieces[r][c] == 0:  # si la case en diagonale est libre
                self.valid_moves.append((r, c))  # se déplacer dans cette case
                r += 1
                c += 1
            else:
                if pieces[r][c].color != White:  # Modification ici pour vérifier si la pièce est blanche
                    self.capture_piece(pieces[r][c])
                    self.valid_moves.append((r, c))  # Manger la pièce
                    break  # Ensuite sortir de la boucle
                else:
                    break  # Sinon déjà s'arrêter à la position actuelle

        # Coups en diagonale
        r = self.r - 1
        c = self.c - 1

        while r >= 0 and c >= 0:  # déplacement vers la gauche tant que r et c sont positifs
            if pieces[r][c] == 0:  # si la case en diagonale est libre
                self.valid_moves.append((r, c))  # se déplacer dans cette case
                r -= 1
                c -= 1
            else:
                if pieces[r][c].color != White:  # Modification ici pour vérifier si la pièce est blanche
                    self.capture_piece(pieces[r][c])
                    self.valid_moves.append((r, c))  # Manger la pièce
                    break  # Ensuite sortir de la boucle
                else:
                    break  # Sinon déjà s'arrêter à la position actuelle

        r = self.r + 1  # Diagonale ligne qui augmente et colonne qui diminue
        c = self.c - 1

        while r <= 7 and c >= 0:
            if pieces[r][c] == 0:  # si la case en diagonale est libre
                self.valid_moves.append((r, c))  # se déplacer dans cette case
                r += 1
                c -= 1
            else:
                if pieces[r][c].color != White:  # Modification ici pour vérifier si la pièce est blanche
                    self.capture_piece(pieces[r][c])
                    self.valid_moves.append((r, c))  # Manger la pièce
                    break  # Ensuite sortir de la boucle
                else:
                    break  # Sinon déjà s'arrêter à la position actuelle

        r = self.r - 1  # Diagonale ligne qui diminue et colonne qui augmente
        c = self.c + 1

        while r >= 0 and c <= 7:
            if pieces[r][c] == 0:  # si la case en diagonale est libre
                self.valid_moves.append((r, c))  # se déplacer dans cette case
                r -= 1
                c += 1
            else:
                if pieces[r][c].color != White:  # Modification ici pour vérifier si la pièce est blanche
                    self.capture_piece(pieces[r][c])
                    self.valid_moves.append((r, c))  # Manger la pièce
                    break  # Ensuite sortir de la boucle
                else:
                    break  # Sinon déjà s'arrêter à la position actuelle

        return self.valid_moves

class King(WWhite):  # King ou Roi est une classe fille de White
    def __init__(self, r, c, color):
        super().__init__(r, c, color)

    def possible_moves(self, pieces):
        self.clear_moves() 

        # Coups Verticaux   
        if self.r - 1 >= 0 :
            if pieces[self.r - 1][self.c] == 0 or pieces[self.r - 1][self.c].color != White:
                self.capture_piece(pieces[self.r - 1][self.c])
                self.valid_moves.append((self.r - 1, self.c))

        if self.r + 1 <= 7:
            if pieces[self.r + 1][self.c] == 0 or pieces[self.r + 1][self.c].color != White:
                self.capture_piece(pieces[self.r + 1][self.c])
                self.valid_moves.append((self.r + 1, self.c))

        # Coups horizontaux           
        if self.c - 1 >= 0:
            if pieces[self.r][self.c - 1] == 0 or pieces[self.r][self.c - 1].color != White:
                self.valid_moves.append((self.r, self.c - 1))

        if self.c + 1 <= 7:
            if pieces[self.r][self.c + 1] == 0 or pieces[self.r][self.c + 1].color != White:
                self.valid_moves.append((self.r, self.c + 1))

        # Coups en diagonale
        if self.r - 1 >= 0 and self.c - 1 >= 0:
            if pieces[self.r - 1][self.c - 1] == 0 or pieces[self.r - 1][self.c - 1].color != White:
                self.valid_moves.append((self.r - 1, self.c - 1))

        if self.r - 1 >= 0 and self.c + 1 <= 7:
            if pieces[self.r - 1][self.c + 1] == 0 or pieces[self.r - 1][self.c + 1].color != White:
                self.valid_moves.append((self.r - 1, self.c + 1))

        if self.r + 1 <= 7 and self.c + 1 <= 7:
            if pieces[self.r + 1][self.c + 1] == 0 or pieces[self.r + 1][self.c + 1].color != White:
                self.valid_moves.append((self.r + 1, self.c + 1))

        if self.r + 1 <= 7 and self.c - 1 >= 0:
            if pieces[self.r + 1][self.c - 1] == 0 or pieces[self.r + 1][self.c - 1].color != White:
                self.valid_moves.append((self.r + 1, self.c - 1))

        return self.valid_moves

