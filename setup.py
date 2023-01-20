import pygame, sys
from pygame.math import Vector2
import random

class Fruit:
    def __init__(self):
        self.randomize()


    def draw_fruit(self):
        # create a rect for the fruit and draw it
        fruit_rect = pygame.Rect(self.position.x*cell_size, self.position.y*cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, 'red', fruit_rect)

    def randomize(self):
        # creates a random position vector
        self.x = random.randint(0, cell_number-1)
        self.y = random.randint(0, cell_number-1)
        self.position = Vector2(self.x, self.y)

class Snake:
    def __init__(self):
        # create the body of a snake with 3 blocks length
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]  # each element is a position vector
        self.direction = Vector2(1,0)
        self.new_block = False

    def draw_snake(self):
        for block in self.body:
            x_pos = block.x*cell_size
            y_pos = block.y*cell_size
            snake_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen, (104, 71, 141), snake_rect)

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

class Main:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    def check_collision(self):
        # checks if the snake ate the fruit and then add a new block to the body
        if self.fruit.position == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()

    def check_fail(self):
        # checks if the snake hits the walls
        if self.snake.body[0].x < 0 or self.snake.body[0].x >= cell_number:
            self.game_over()
        if self.snake.body[0].y < 0 or self.snake.body[0].y >= cell_number:
            self.game_over()

        # checks if the snake hits its own body
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit()




# general settings
pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_size*cell_number, cell_size*cell_number))
clock = pygame.time.Clock()


surface = pygame.Surface((100, 200))
surface.fill('blue')
test_rect = surface.get_rect(center=(200, 250))

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = Main()

while True:
    # check player input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1,0)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1,0)

def idiota():
    print('aaa')

    screen.fill((0, 154, 23))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)
