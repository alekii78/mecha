import sys

import pygame,random
from pygame.math import Vector2

# initializing pygame
pygame.init()
# creating title of the game
title_font=pygame.font.Font(None,60)
# displaying score on the screen
score_font=pygame.font.Font(None,40)
GREEN=(103,104,196)
DARK_GREEN=(43,51,24)
# creating cells
cell_size=30
nUmber_of_cells=25
OFFSET=25

class Game:
    def __init__(self):
        self.snake=Snake()
        self.food=Food(self.snake.body)
        self.state="RUNNING"
        self.score=0

    def draw(self):
        self.food.draw()
        self.snake.draw()

    def update(self):
        if self.state=="RUNNING":
            self.snake.update()
            self.check_collision_with_food()
            self.check_collision_with_edges()
            self.check_collision_with_tail()

    def game_over(self):
        self.snake.reset()
        self.food.position=self.food.generate_random_pos(self.snake.body)
        self.state="STOPPED"
        self.score=0


    def check_collision_with_food(self):
        if self.snake.body[0]==self.food.position:
          self.food.position=self.food.generate_random_pos(self.snake.body)
          self.snake.add_segment=True
          self.score +=1
    def check_collision_with_edges(self):
        if self.snake.body[0].x==nUmber_of_cells or self.snake.body[0].x==-1:
            self.game_over()
        if self.snake.body[0].y==nUmber_of_cells or self.snake.body[0].y==-1:
            self.game_over()
    def check_collision_with_tail(self):
        headless_body=self.snake.body[1:]
        # checks whether tail and head are the same
        # you can rename headles_body as the tail
        if self.snake.body[0] in headless_body:
            self.game_over()



# creating class food
class Food:
    def __init__(self,snake_body):
       self.position=self.generate_random_pos(snake_body)

    def draw(self):
        food_rect=pygame.Rect(OFFSET+self.position.x*cell_size,OFFSET+self.position.y*cell_size,cell_size,cell_size)
        pygame.draw.rect(screen,DARK_GREEN,food_rect)
        # blit() method draws image on the screen
        screen.blit(food_surfce,food_rect)

    def generate_random_cell(self):
        x = random.randint(0, nUmber_of_cells - 1)
        y = random.randint(0, nUmber_of_cells - 1)
        return  Vector2(x,y)

    def generate_random_pos(self,snake_body):

        position=self.generate_random_cell()
        while position in snake_body:
            position=self.generate_random_cell()

        return position

# creating snake class
class Snake:
    def __init__(self):
        self.body=[Vector2(6,9),Vector2(5,9),Vector2(4,9)]
        self.direction=Vector2(1,0)
        self.add_segment=False

    def draw(self):
        for segment in self.body:
            segment_rect=(OFFSET+segment.x*cell_size,OFFSET+segment.y*cell_size,cell_size,cell_size)
            pygame.draw.rect(screen,DARK_GREEN,segment_rect,0,7)

        #drawing  update for snake to move
    def update(self):
        self.body = self.body.insert(0, self.body[0] + self.direction)

        if self.add_segment==True:

            self.add_segment=False

        else:
            self.body=self.body[:-1]
            # remove one point
    def reset(self):
        self.body=[Vector2(6,9),Vector2(5,9),Vector2(4,9)]
        self.direction=Vector2(1,0)




# settting screen
screen=pygame.display.set_mode((2*OFFSET+cell_size*nUmber_of_cells,2*OFFSET+ cell_size*nUmber_of_cells))
pygame.display.set_caption("snake game by Alex ")
clock=pygame.time.Clock()

game=Game()
food_surfce=pygame.image.load("C:\\Users\\njugu\PycharmProjects\\try\\venv\\Scripts\\try_open_cv\\videos and pic\\logo.jpg",)

SNAKE_UPDATE=pygame.USEREVENT
pygame.time.set_timer(SNAKE_UPDATE,200)
# game loop
while True:
    # call for an event
    for event in pygame.event.get():
        if event.type==SNAKE_UPDATE:
            game.update()
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type==pygame.KEYDOWN:
            if game.state=="STOPPED":
                game.state="RUNNING"
            if event.key==pygame.K_UP and game.snake.direction !=Vector2(0,1):
                # when user presses up key
                game.snake.direction=Vector2(0,-1)
            if event.key==pygame.K_DOWN and game.snake.direction !=Vector2(0,-1):
                game.snake.direction=Vector2(0,1)
            if event.key==pygame.K_LEFT and game.snake.direction !=Vector2(1,0):
                game.snake.direction=Vector2(-1,0)

            if event.key==pygame.K_RIGHT and game.snake.direction !=Vector2(-1,0):
                game.snake.direction=Vector2(1,0)


# tick () method  to set time
        screen.fill(GREEN)
        # fill() fill the screen with the color
        pygame.draw.rect(screen,DARK_GREEN,(OFFSET-5,OFFSET-5,cell_size*nUmber_of_cells+10,cell_size*nUmber_of_cells+10),5)
        game.draw()
        title_surface=title_font.render("PYGAME SNAKE BY ALEX",True,DARK_GREEN)
        score_surface=score_font.render(str(game.score),True,DARK_GREEN)

        screen.blit(title_surface,(OFFSET-5,20))
        screen.blit(score_surface,(OFFSET-5,OFFSET+ cell_size*nUmber_of_cells+10))
        pygame.display.update()
        clock.tick(60)
