import sys  # Import the sys module for interacting with the Python runtime
import random  # Import the random module for generating random numbers
import pygame  # Import the pygame module for creating the game

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480  # Set the width and height of the game screen
SIZE = 80  # Set the size of each square on the game board
BOARD_ROWS = 6  # Set the number of rows on the game board
BOARD_COLS = 7  # Set the number of columns on the game board
RACK_ROWS = 2  # Set the number of rows in the player's rack
RACK_COLS = 7  # Set the number of columns in the player's rack

# Set up some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Create the game screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Three in a Row")

# Create the game board
board = [[0 for col in range(BOARD_COLS)] for row in range(BOARD_ROWS)]

# Create the player's rack
rack = [[0 for col in range(RACK_COLS)] for row in range(RACK_ROWS)]

# Create a function to draw the game board
def draw_board():
  for row in range(BOARD_ROWS):
    for col in range(BOARD_COLS):
      if board[row][col] == 1:
        pygame.draw.rect(screen, RED, pygame.Rect(col * SIZE, row * SIZE, SIZE, SIZE))
      elif board[row][col] == 2:
        pygame.draw.rect(screen, GREEN, pygame.Rect(col * SIZE, row * SIZE, SIZE, SIZE))

# Create a function to draw the player's rack
def draw_rack():
  for row in range(RACK_ROWS):
    for col in range(RACK_COLS):
      if rack[row][col] > 0:
        pygame.draw.rect(screen, BLUE, pygame.Rect(col * SIZE, row * SIZE, SIZE, SIZE))
        pygame.draw.text(screen, str(rack[row][col]), (col * SIZE + 10, row * SIZE + 10), WHITE)

# Create a function to check for a win
def check_win():
  # Check horizontal, vertical, and diagonal lines for three in a row
  for row in range(BOARD_ROWS - 2):
    for col in range(BOARD_COLS):
      if board[row][col] > 0 and board[row][col] == board[row + 1][col] == board[row + 2][col]:
        return True
  for row in range(BOARD_ROWS):
    for col in range(BOARD_COLS - 2):
      if board[row][col] >
      