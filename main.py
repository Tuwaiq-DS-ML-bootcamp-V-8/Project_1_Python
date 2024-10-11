import pygame
from pygame.locals import *
import time
import random

# Checks if the cards match using their array indices
def match_check(deck, flipped):
    return deck[6 * flipped[0][1] + flipped[0][0]] == deck[6 * flipped[1][1] + flipped[1][0]]

def main_menu():
    pygame.init()
    display_size = (750, 905)
    screen = pygame.display.set_mode(display_size)
    pygame.display.set_caption("Memory Match Main Menu")

    font = pygame.font.Font(None, 50)

    solo_button = pygame.Rect(275, 300, 200, 50)
    friend_button = pygame.Rect(275, 400, 200, 50)
    exit_button = pygame.Rect(275, 500, 200, 50)

    while True:  # Use this instead of 'running' variable
        screen.fill((255, 255, 255))  # White background

        # Render buttons
        pygame.draw.rect(screen, (0, 0, 0), solo_button)
        pygame.draw.rect(screen, (0, 0, 0), friend_button)
        pygame.draw.rect(screen, (0, 0, 0), exit_button)

        # Add text to buttons
        screen.blit(font.render("Play Solo", True, (255, 255, 255)), (solo_button.x + 20, solo_button.y + 10))
        screen.blit(font.render("Play with a Friend", True, (255, 255, 255)), (friend_button.x + 10, friend_button.y + 10))
        screen.blit(font.render("Exit", True, (255, 255, 255)), (exit_button.x + 70, exit_button.y + 10))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if solo_button.collidepoint(event.pos):
                    main(0)  # Start the solo game
                elif friend_button.collidepoint(event.pos):
                    two_player_mode()  # Start the two-player mode
                elif exit_button.collidepoint(event.pos):
                    pygame.quit()
                    quit()

def two_player_mode():
    display_size = (750, 905)
    pygame.init()
    screen = pygame.display.set_mode(display_size)
    pygame.display.set_caption("Two Player Mode")

    # The decks are removed since they aren't being used
    # player1_deck = cards_init()
    # player2_deck = cards_init()

    # Timers removed since they aren't being used
    # player1_timer = 60  # 60 seconds
    # player2_timer = 60  # 60 seconds

    game_run = True
    while game_run:
        screen.fill((255, 255, 255))

        # Draw the dividing line between two halves
        pygame.draw.line(screen, (0, 0, 0), (375, 0), (375, 905), 5)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_run = False
                pygame.quit()



# Get mouse position, and check which card it's on using division
def card_check(mouse_pos):
    mousex = mouse_pos[0]
    mousey = mouse_pos[1]
    cardx = int(mousex / 125)
    cardy = int(mousey / 181)
    card = (cardx, cardy)
    return card


# Draw the cards. This is used after initialization and to rehide cards
def card_draw(cards):
    pygame.init()
    display_size = (750, 905)
    screen = pygame.display.set_mode(display_size)

    # Place card images in their appropriate spots by multiplying card width & height
    for i in range(6):
        for j in range(5):
            screen.blit(cards[i + 6 * j], (i * 125, j * 181))


# Load the main card images (used in cards_init())
def load_card_image(char):  # Renamed from 'card_load' to avoid name shadowing
    card = f"./card_images/{char}-spades.png"
    card_load = pygame.image.load(card)
    return card_load


def cards_init():
    cards = []

    # Load images into array
    for i in range(2, 11):
        cards.append(load_card_image(i))

    for alpha in ['J', 'Q', 'K', 'A']:
        cards.append(load_card_image(alpha))

    cards.append(load_card_image('wild'))
    joker_load = pygame.image.load("./card_images/joker.png")
    cards.append(joker_load)

    # Multiply the deck by two so there is one pair of everything
    cards *= 2  # Python is great - just double the list to duplicate!

    # Shuffle the deck for a new game every time
    random.shuffle(cards)

    return cards


def main(runs):
    display_size = (750, 905)
    game_title = "Python Memory Match"
    desired_fbs = 60

    # Setup preliminary pygame stuff
    pygame.init()
    screen = pygame.display.set_mode(display_size)
    pygame.display.set_caption(game_title)

    fps_clock = pygame.time.Clock()

    card_deck = cards_init()  # initialize deck

    # Load card-back image for all cards at first, and have matches slowly unveiled
    card_back = pygame.image.load("./card_images/card_back.png")
    visible_deck = [card_back] * 30

    card_draw(visible_deck)

    game_run = True  # run the game

    if runs == 0:
        print("Welcome to Memory Match! Select two cards to flip them and find a match!")
        print("Press 'q' to quit at any time.")
    elif runs == 1:
        print("\n\nNew Game")

    flips = []
    found = []
    missed = 0
    first_flip = 0
    second_flip = 0
    t = 1

    while game_run:
        user_input = pygame.event.get()
        pressed_key = pygame.key.get_pressed()

        for event in user_input:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                card_select = card_check(mouse_pos)

                if card_select not in flips and card_select not in found:
                    flips.append(card_select)
                    if len(flips) <= 2:
                        screen.blit(card_deck[6 * card_select[1] + card_select[0]],
                                    (125 * card_select[0], 181 * card_select[1]))
                        first_flip = time.time()  # First card has been flipped
                    if len(flips) == 2:
                        second_flip = time.time()  # Second card has been flipped
                        match = match_check(card_deck, flips)
                        if match:
                            for i in range(2):
                                found.append(flips[i])
                                visible_deck[6 * flips[i][1] + flips[i][0]] = card_deck[6 * flips[i][1] + flips[i][0]]
                            print(f"Matches found: {len(found) // 2}/15")
                            t = 0
                        else:
                            missed += 1

        if len(flips) >= 2 and time.time() - second_flip > t:
            t = 1
            card_draw(visible_deck)
            flips = []

        elif len(flips) == 1 and time.time() - first_flip > 3:
            card_draw(visible_deck)
            flips = []

        pygame.display.flip()
        fps_clock.tick(desired_fbs)

        if pressed_key[K_q]:
            game_run = False

        if len(found) == 30:
            print("YOU WIN!")
            print(f"Score: {missed} misses")
            print("\nPlay again? (y/n)")
            runs = 2

        if runs == 2:  # Win condition loop
            again = input("Play again? (y/n): ").lower()
            if again == "y":
                main(1)
            else:
                print("Thanks for playing!")
                pygame.quit()


if __name__ == "__main__":
    main_menu()
