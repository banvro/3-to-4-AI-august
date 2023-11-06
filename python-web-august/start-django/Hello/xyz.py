import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
FPS = 10

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Initialize clock
clock = pygame.time.Clock()

class Snake:
    def __init__(self):
        self.body = [(100, 50), (90, 50), (80, 50)]
        self.direction = (CELL_SIZE, 0)  # Start moving right

    def move(self, food):
        head = (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])
        self.body.insert(0, head)

        # Check if the snake ate the food
        if self.body[0] == food:
            return True
        else:
            self.body.pop()
            return False

    def change_direction(self, new_direction):
        if new_direction == "UP" and self.direction != (0, CELL_SIZE):
            self.direction = (0, -CELL_SIZE)
        if new_direction == "DOWN" and self.direction != (0, -CELL_SIZE):
            self.direction = (0, CELL_SIZE)
        if new_direction == "LEFT" and self.direction != (CELL_SIZE, 0):
            self.direction = (-CELL_SIZE, 0)
        if new_direction == "RIGHT" and self.direction != (-CELL_SIZE, 0):
            self.direction = (CELL_SIZE, 0)

class Food:
    def __init__(self):
        self.position = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))

    def spawn_food(self):
        self.position = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))

snake = Snake()
food = Food()
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction("UP")
            elif event.key == pygame.K_DOWN:
                snake.change_direction("DOWN")
            elif event.key == pygame.K_LEFT:
                snake.change_direction("LEFT")
            elif event.key == pygame.K_RIGHT:
                snake.change_direction("RIGHT")

    food_eaten = snake.move(food.position)

    if food_eaten:
        food.spawn_food()

    # Collision checks (game over)
    if (snake.body[0][0] < 0 or snake.body[0][0] >= WIDTH or
        snake.body[0][1] < 0 or snake.body[0][1] >= HEIGHT or
        snake.body[0] in snake.body[1:]):
        game_over = True

    screen.fill(WHITE)

    # Draw snake
    for segment in snake.body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], CELL_SIZE, CELL_SIZE))

    # Draw food
    pygame.draw.rect(screen, RED, pygame.Rect(food.position[0], food.position[1], CELL_SIZE, CELL_SIZE))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()

sys.exit()
