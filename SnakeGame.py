import pygame
from pygame.locals import *
import time
import random

class Game():
    
    def __init__(self):
        self.window_x = 720
        self.window_y = 640
        self.background_colour = (232, 12, 232)
        self.score = 0
        self.speed = 0.1
        self.game_surface = pygame.display.set_mode((self.window_x,self.window_y))
        self.game_surface.fill((self.background_colour))
        self.snake = Snake(self.game_surface)
        self.food = Food(self.game_surface)
        self.obstacles = Obstacle(self.game_surface,3)
    
    def check_gameover(self):
        for i in range(0,self.snake.snake_length-1):
            if self.snake.coordinate_x[0] == self.snake.coordinate_x[i+1] and self.snake.coordinate_y[0] == self.snake.coordinate_y[i+1]:
                return True
        for j in range(0,self.obstacles.numof_obs):
            if self.snake.coordinate_x[0] == self.obstacles.coord_x[j] and self.snake.coordinate_y[0] == self.obstacles.coord_y[j]:
                return True
        return False    
    def game_over(self):
        myfont = pygame.font.SysFont("monospace", 30)
        losetext = myfont.render("You Lost! and Your Score: " + str(self.score), 3, (12, 13, 13))
        self.game_surface.blit(losetext,(120,300))
        pygame.display.update()
        time.sleep(5)

    def check_the_food(self):
        if self.snake.coordinate_x[0] == self.food.coord_x and self.snake.coordinate_y[0] == self.food.coord_y:
            self.snake.lengthen_the_snake()
            self.snake.snake_length += 1
            self.score += 1
            self.speed -= 0.002
            self.food.change_the_location()
            self.obstacles.change_location()

    def show_score(self):
        myfont = pygame.font.SysFont("monospace", 20)
        scoretext = myfont.render("Score = "+str(self.score), 3, (0,0,0))
        self.game_surface.blit(scoretext,(5,10))

    def run(self):
        pygame.init()
        running = True
        while running:
            for event in pygame.event.get():

                if event.type == KEYDOWN:

                    if event.key == K_ESCAPE:
                        running = False
                        exit()

                    elif event.key == K_UP:
                        self.snake.move_up()

                    elif event.key == K_DOWN:
                        self.snake.move_down()

                    elif event.key == K_RIGHT:
                        self.snake.move_right()

                    elif event.key == K_LEFT:
                        self.snake.move_left()

                elif event.type == QUIT:
                    running = False
                    exit()
           
            self.snake.move()
            self.food.draw()
            self.obstacles.draw()
            self.check_the_food()
            self.show_score() 
            if self.check_gameover():
                self.game_over()
                running = False
                exit()
            pygame.display.update()
            time.sleep(self.speed)


class Snake():
    def __init__(self,screen, length=1):
        self.snake_length = length
        self.snake_direction = "right"
        self.background_colour = (232, 12, 232)
        self.screen = screen
        self.snake_size = 20
        self.snake_colour = (237, 230, 14)
        self.coordinate_x = []
        self.coordinate_y = []
        self.create_snake()
    
    def lengthen_the_snake(self):
        self.coordinate_x.append(0)
        self.coordinate_y.append(0)

    def create_snake(self):
        for j in range(self.snake_length): 
            self.coordinate_x.append(200 - j*20)
            self.coordinate_y.append(40)

    def draw(self):
        self.screen.fill(self.background_colour)
        self.snake_draw = pygame.draw.rect(self.screen,self.snake_colour,[self.coordinate_x[0],self.coordinate_y[0],self.snake_size,self.snake_size])

        for i in range(self.snake_length-1): 
            pygame.draw.rect(self.screen,"green",[self.coordinate_x[i+1],self.coordinate_y[i+1],self.snake_size,self.snake_size])
           
        

    def control_borders(self):
        if self.coordinate_x[0] > 720:
            self.coordinate_x[0] = 0

        if self.coordinate_x[0] < 0:
            self.coordinate_x[0] = 720

        if self.coordinate_y[0] > 640:
            self.coordinate_y[0] = 0

        if self.coordinate_y[0] < 0:
            self.coordinate_y[0] = 640

    def move(self):

        self.control_borders()

        for i in range(self.snake_length-1,0,-1):
            self.coordinate_x[i] = self.coordinate_x[i-1]
            self.coordinate_y[i] = self.coordinate_y[i-1] 

        if self.snake_direction == "up":
            self.coordinate_y[0] -= self.snake_size
            self.draw()

        if self.snake_direction == "down":
            self.coordinate_y[0] += self.snake_size
            self.draw()
        
        if self.snake_direction == "right":
            self.coordinate_x[0] += self.snake_size
            self.draw()

        if self.snake_direction == "left":
            self.coordinate_x[0] -= self.snake_size
            self.draw()

    def move_up(self):
        if self.snake_direction != "down":
            self.snake_direction = "up"

    def move_down(self):
        if self.snake_direction != "up": 
            self.snake_direction = "down"

    def move_right(self):
        if self.snake_direction != "left":
            self.snake_direction = "right"

    def move_left(self):
        if self.snake_direction != "right":
            self.snake_direction = "left"

class Food():

    def __init__(self,screen):
        self.food_size = 20
        self.food_colour = (245, 7, 7)
        self.coord_x = 80
        self.coord_y = 120
        self.screen = screen
        self.draw()

    def draw(self):
        self.draw_food = pygame.draw.rect(self.screen,self.food_colour,[self.coord_x,self.coord_y,self.food_size,self.food_size]) 

    def change_the_location(self):
        self.coord_x = random.randint(1,35)*self.food_size
        self.coord_y = random.randint(1,31)*self.food_size
    
class Obstacle():

    def __init__(self,screen,numof_obs = 1):
        self.obstacle_size = 20
        self.obstacle_colour = (0,0,255)
        self.coord_x = []
        self.coord_y = []
        self.screen = screen
        self.numof_obs = numof_obs
        self.create_obstacles()
        self.draw()
    def draw(self):
        for i in range(0,self.numof_obs):
             pygame.draw.rect(self.screen,self.obstacle_colour,[self.coord_x[i],self.coord_y[i],self.obstacle_size,self.obstacle_size])

    def create_obstacles(self):
        for j in range(0,self.numof_obs):
            self.coord_x.append(random.randint(1,35)*self.obstacle_size)
            self.coord_y.append(random.randint(1,31)*self.obstacle_size)

    def change_location(self):
        numb = random.randint(0,self.numof_obs-1)
        self.coord_x[numb] = random.randint(1,35)*self.obstacle_size
        self.coord_y[numb] = random.randint(1,31)*self.obstacle_size
if __name__ == "__main__":
    game = Game()
    game.run()
