def evaluation(pieces):
   

    piece_value = {'K': 0, 'Q': 900, 'R': 500, 'B': 330, 'N': 320, 'p': 100}
    score = 0
    for row in pieces:
        for square in row:
            if square != "None":
                piece_type = square[1]
                piece_color = square[0]
                value = piece_value[piece_type]
                score += value if piece_color == 'w' else -value
    return score


#Code inachevé pour l'implémentation de l'algorithme Minamax (technique d'optimisation égalage alpha bêta)