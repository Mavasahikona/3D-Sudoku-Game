import pygame
import sys
import random
import sqlite3
from pygame.locals import *

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D Sudoku Game")
clock = pygame.time.Clock()

# Database setup for score tracking
def init_db():
    conn = sqlite3.connect('scores.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS scores
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      player_name TEXT,
                      score INTEGER,
                      difficulty TEXT,
                      timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

# Initialize the database
init_db()

# Game states
MENU = 0
PLAYING = 1
GAME_OVER = 2

# Current game state
current_state = MENU

# Difficulty levels
DIFFICULTY_EASY = "Easy"
DIFFICULTY_MEDIUM = "Medium"
DIFFICULTY_HARD = "Hard"

# Current difficulty
current_difficulty = DIFFICULTY_EASY

# Score
score = 0

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.fill(WHITE)

    if current_state == MENU:
        # Render menu
        font = pygame.font.Font(None, 36)
        title = font.render("3D Sudoku Game", True, BLACK)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 100))

        easy = font.render("1. Easy", True, BLACK)
        screen.blit(easy, (WIDTH // 2 - easy.get_width() // 2, 200))

        medium = font.render("2. Medium", True, BLACK)
        screen.blit(medium, (WIDTH // 2 - medium.get_width() // 2, 250))

        hard = font.render("3. Hard", True, BLACK)
        screen.blit(hard, (WIDTH // 2 - hard.get_width() // 2, 300))

        # Handle menu input
        keys = pygame.key.get_pressed()
        if keys[K_1]:
            current_difficulty = DIFFICULTY_EASY
            current_state = PLAYING
        elif keys[K_2]:
            current_difficulty = DIFFICULTY_MEDIUM
            current_state = PLAYING
        elif keys[K_3]:
            current_difficulty = DIFFICULTY_HARD
            current_state = PLAYING

    elif current_state == PLAYING:
        # Render game
        font = pygame.font.Font(None, 24)
        difficulty_text = font.render(f"Difficulty: {current_difficulty}", True, BLACK)
        screen.blit(difficulty_text, (20, 20))

        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (20, 50))

    elif current_state == GAME_OVER:
        # Render game over screen
        font = pygame.font.Font(None, 36)
        game_over = font.render("Game Over!", True, RED)
        screen.blit(game_over, (WIDTH // 2 - game_over.get_width() // 2, 200))

        final_score = font.render(f"Final Score: {score}", True, BLACK)
        screen.blit(final_score, (WIDTH // 2 - final_score.get_width() // 2, 250))
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()