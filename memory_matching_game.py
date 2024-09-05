import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 4
CARD_SIZE = WIDTH // GRID_SIZE
CARD_BACK_COLOR = (255, 255, 255)
CARD_FRONT_COLOR = (0, 128, 255)
CARD_TEXT_COLOR = (255, 255, 255)
FPS = 30

# Font
FONT = pygame.font.Font(None, 50)

# Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Memory Matching Game')

# Generate a list of card pairs
def generate_cards():
    numbers = list(range(1, (GRID_SIZE ** 2 // 2) + 1)) * 2
    random.shuffle(numbers)
    return [numbers[i:i + GRID_SIZE] for i in range(0, len(numbers), GRID_SIZE)]

# Draw card
def draw_card(x, y, value, revealed=False):
    rect = pygame.Rect(x * CARD_SIZE, y * CARD_SIZE, CARD_SIZE, CARD_SIZE)
    pygame.draw.rect(screen, CARD_BACK_COLOR if not revealed else CARD_FRONT_COLOR, rect)
    pygame.draw.rect(screen, (0, 0, 0), rect, 2)
    if revealed:
        text = FONT.render(str(value), True, CARD_TEXT_COLOR)
        screen.blit(text, (x * CARD_SIZE + CARD_SIZE // 2 - text.get_width() // 2, y * CARD_SIZE + CARD_SIZE // 2 - text.get_height() // 2))

# Main function
def main():
    clock = pygame.time.Clock()
    cards = generate_cards()
    revealed = [[False] * GRID_SIZE for _ in range(GRID_SIZE)]
    first_card = None
    second_card = None
    game_over = False

    while True:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                x, y = event.pos
                x //= CARD_SIZE
                y //= CARD_SIZE

                if not revealed[y][x]:
                    if first_card is None:
                        first_card = (x, y)
                    elif second_card is None:
                        second_card = (x, y)

                    if first_card and second_card:
                        fx, fy = first_card
                        sx, sy = second_card
                        if cards[fy][fx] == cards[sy][sx]:
                            revealed[fy][fx] = True
                            revealed[sy][sx] = True
                        pygame.time.wait(1000)
                        first_card = None
                        second_card = None

        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                draw_card(x, y, cards[y][x], revealed[y][x])

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
