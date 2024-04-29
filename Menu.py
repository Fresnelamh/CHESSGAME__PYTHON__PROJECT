

import os
import pygame
import sys
import textwrap
from principal import *



pygame.init()


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
font = pygame.font.SysFont(None, 50)
settings_font = pygame.font.SysFont(None, 40, bold=True)
help_font_bold = pygame.font.SysFont(None, 30, bold=True)
help_font_regular = pygame.font.SysFont(None, 30, bold=False)
# Configuration du mixer pour la musique
pygame.mixer.init()
pygame.mixer.music.load("Music/Paradise_Found.mp3")
languages = {
    'en': {
        'settings': "Settings",
        'help': "Help",
        'game_mode': "Game Mode",
        'language': "Language",
        'english': "English",
        'french': "French",
        'start_game': "Start Game",
        'load_game': "Load Game",
        'quit': "Quit"
    },
    'fr': {
        'settings': "Paramètres",
        'help': "Aide",
        'game_mode': "Mode du Jeu",
        'language': "Langue",
        'english': "Anglais",
        'french': "Français",
        'start_game': "Commencer une Partie",
        'load_game': "Charger une Partie",
        'quit': "Quitter"
    }
}

# Langue initiale
current_language = 'fr'  # Remplacez par le chemin de votre fichier musical
  # Rafraîchir l'affichage des paramètres

def change_language(settings_screen):
    global current_language  # Importante pour pouvoir modifier la variable globale
    
    # Création des textes et positions pour les choix de langue
    lang_font = pygame.font.SysFont(None, 35, bold=True)
    english_text = lang_font.render("Anglais", True, BLACK)
    french_text = lang_font.render("Français", True, BLACK)
    english_rect = english_text.get_rect(center=(300, 150))
    french_rect = french_text.get_rect(center=(300, 250))

    choosing = True
    while choosing:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if english_rect.collidepoint(event.pos):
                    current_language = 'en'
                    choosing = False  # Termine la boucle après sélection
                elif french_rect.collidepoint(event.pos):
                    current_language = 'fr'
                    choosing = False  # Termine la boucle après sélection

        settings_screen.fill(WHITE)
        settings_screen.blit(english_text, english_rect)
        settings_screen.blit(french_text, french_rect)
        pygame.display.flip()

    return current_language  # Retourne la nouvelle langue sélectionnée




def start_game():
    print("La partie commence !")
    pygame.mixer.music.stop()
    
  # Arrêter la musique lors du démarrage du jeu

    main()
    main_menu()
    

def load_game():
    print("Chargement de la partie")



def open_statistics():
    print("Statistiques du jeu")

def quit_game():
    pygame.mixer.music.stop()  
    pygame.quit()
    sys.exit()

def resize_image(image, width, height):
    return pygame.transform.scale(image, (width, height))
BEIGE = (245, 245, 220) 


def open_settings():
    print("Paramètres du jeu")
  
    settings_screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Paramètres")
    settings_font = pygame.font.SysFont(None, 40, bold=True)

  
    running = True
    while running:
        
        help_text = settings_font.render(languages[current_language]['help'], True, BLACK)
        game_mode_text = settings_font.render(languages[current_language]['game_mode'], True, BLACK)
        langue_text = settings_font.render(languages[current_language]['language'], True, BLACK)

        help_rect = help_text.get_rect(center=(300, 100))
        game_mode_rect = game_mode_text.get_rect(center=(300, 200))
        langue_rect = langue_text.get_rect(center=(300, 300))

        settings_screen.fill(BEIGE)
        settings_screen.blit(help_text, help_rect)
        settings_screen.blit(game_mode_text, game_mode_rect)
        settings_screen.blit(langue_text, langue_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
           
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if help_rect.collidepoint(event.pos):
                    open_help()  # Appelle la fonction d'aide lorsque vous cliquez sur "Aide"
                elif game_mode_rect.collidepoint(event.pos):
                    # Ajoutez ici votre logique pour le mode de jeu si nécessaire
                    pass
                elif langue_rect.collidepoint(event.pos):
                    change_language(settings_screen)  # Change la langue si on clique sur "Langue"

       
        pygame.display.flip()

def change_language(settings_screen):
    lang_font = pygame.font.SysFont(None, 35, bold=True)
    english_text = lang_font.render("English", True, BLACK)
    french_text = lang_font.render("Français", True, BLACK)

    english_rect = english_text.get_rect(center=(300, 150))
    french_rect = french_text.get_rect(center=(300, 250))

    choosing = True
    while choosing:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if english_rect.collidepoint(event.pos):
                    global current_language
                    current_language = 'en'
                    return  # Retourne immédiatement après le changement de langue
                elif french_rect.collidepoint(event.pos):
                    current_language = 'fr'
                    return  # Retourne immédiatement après le changement de langue

        settings_screen.fill(WHITE)
        settings_screen.blit(english_text, english_rect)
        settings_screen.blit(french_text, french_rect)
        pygame.display.flip()


                 

   

      

def open_help():
    # Création de la fenêtre
    help_screen = pygame.display.set_mode((700, 700))
    pygame.display.set_caption("Règles du jeu d'échecs")

    # Polices
    help_font_bold = pygame.font.SysFont(None, 30, bold=True)
    help_font_regular = pygame.font.SysFont(None, 30, bold=False)

    # Règles du jeu d'échecs
    rules_text = [
        ("Règles du jeu d'échecs", True),
        ("Objectif du jeu: Le but est de mettre en échec et mat le roi de l'adversaire, ce qui signifie que le roi est en position d'être capturé ('échec') et ne peut pas échapper à la capture.", False),
        ("Déplacement des pièces: Chaque type de pièce se déplace différemment. Les pions avancent d'une case vers l'avant, mais capturent en diagonale. Les tours se déplacent en ligne droite horizontalement ou verticalement. Les cavaliers se déplacent en 'L'. Les fous se déplacent en diagonale. La dame peut se déplacer horizontalement, verticalement ou diagonalement. Le roi se déplace d'une case dans n'importe quelle direction.", False),
        ("Échec et Mat: Si un roi est en échec et qu'il ne peut pas se déplacer vers une case sans être en échec, alors il est en 'échec et mat' et la partie est terminée. Le joueur qui a capturé le roi adverse gagne la partie.", False),
        ("Fin de partie: La partie peut se terminer par un échec et mat, un nul.", False),
    
    ]

    def draw_text():
        help_screen.fill(BEIGE)
        y = 50
        for text, is_bold in rules_text:
            font = help_font_bold if is_bold else help_font_regular
            wrapped_text = textwrap.wrap(text, width=60)
            for line in wrapped_text:
                text_surface = font.render(line, True, BLACK)
                help_screen.blit(text_surface, (50, y))
                y += 30
        pygame.display.flip()

    # Dessiner le texte initial
    draw_text()

    # Boucle principale
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Clic gauche
                    if event.pos[1] < 30:
                        # Maximiser la fenêtre
                        help_screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                        draw_text()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

    # Quitter Pygame
    pygame.quit()






    




def main_menu():
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Menu du jeu d'échecs")
    clock = pygame.time.Clock()

  
    pygame.mixer.music.play(-1)

 
    background_image = pygame.image.load("img/background.jpg").convert()
    background_image = resize_image(background_image, 800, 600)

 
    font = pygame.font.SysFont(None, 50)
    start_text = font.render("Commencer une partie", True, BLACK)
    load_text = font.render("Charger une partie", True, BLACK)
    settings_text = font.render("Paramètres", True, BLACK)
    statistics_text = font.render("Statistiques", True, BLACK)
    quit_text = font.render("Quitter", True, BLACK)
   

 
    start_rect = start_text.get_rect(center=(400, 150))
    load_rect = load_text.get_rect(center=(400, 250))
    settings_rect = settings_text.get_rect(center=(400, 350))
    statistics_rect = statistics_text.get_rect(center=(400, 450))
    quit_rect = quit_text.get_rect(center=(400, 550))

    running = True
    while running:
        screen.fill(WHITE)
        screen.blit(background_image, (0, 0))

        screen.blit(start_text, start_rect)
        screen.blit(load_text, load_rect)
        screen.blit(settings_text, settings_rect)
        screen.blit(statistics_text, statistics_rect)
        screen.blit(quit_text, quit_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if start_rect.collidepoint(mouse_pos):
                    start_game()
                elif load_rect.collidepoint(mouse_pos):
                    load_game()
                elif settings_rect.collidepoint(mouse_pos):
                    open_settings()
                elif statistics_rect.collidepoint(mouse_pos):
                    open_statistics()
                elif quit_rect.collidepoint(mouse_pos):
                    quit_game()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main_menu()



def save_game(state, filename="saved_game.json"):
    with open(filename, 'w') as file:
        json.dump(state, file)
    main_menu()

def load_game_state(filename="saved_game.json"):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return None

def display_saved_games():
 
    saved_games = [f for f in os.listdir() if f.startswith("saved_game") and f.endswith(".json")]
    return saved_games


def load_game():
    print("Chargement de la partie...")
    saved_games = display_saved_games()
    if not saved_games:
        print("Aucune partie sauvegardée trouvée.")
        return

  
    print("Parties sauvegardées :")
    for i, game in enumerate(saved_games):
        print(f"{i + 1}. {game}")

   
    choice = int(input("Entrez le numéro de la partie à charger : ")) - 1
    if 0 <= choice < len(saved_games):
        game_state = load_game_state(saved_games[choice])
        print("Partie chargée avec succès.")
      
    else:
        print("Choix invalide.")

















































































import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Configuration de la fenêtre
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mon Jeu")

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Police de caractères pour le texte
font = pygame.font.SysFont(None, 50)

def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'  # Retourner 'quit' pour quitter l'application
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Gérer les interactions avec le menu ici (ex : clic sur les boutons)
                pass

        screen.fill(BLACK)
        menu_text = font.render("Press ENTER to Start, ESC to Quit", True, WHITE)
        screen.blit(menu_text, (50, 300))
        pygame.display.flip()

def game_loop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'main_menu'  # Retourner 'main_menu' pour retourner au menu principal
            # Gérer d'autres événements ici

        screen.fill(WHITE)
        game_text = font.render("Game is running...", True, BLACK)
        screen.blit(game_text, (50, 300))
        pygame.display.flip()

def main():
    action = 'main_menu'
    while action != 'quit':
        if action == 'main_menu':
            action = main_menu()
        elif action == 'start_game':
            action = game_loop()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()



