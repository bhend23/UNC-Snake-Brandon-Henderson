__author__ = "Brandon Henderson"

import pygame, sys, random
from pygame.math import Vector2


class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direction = Vector2(0,0)
        self.new_block = False

        self.head_up = pygame.image.load(r'/Users/bhtun/summer projects/snake/head_up.png').convert_alpha()
        self.head_down = pygame.image.load(r'/Users/bhtun/summer projects/snake/head_down.png').convert_alpha()
        self.head_right = pygame.image.load(r'/Users/bhtun/summer projects/snake/head_right.png').convert_alpha()
        self.head_left = pygame.image.load(r'/Users/bhtun/summer projects/snake/head_left.png').convert_alpha()

        self.tail_up = pygame.image.load(r'/Users/bhtun/summer projects/snake/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load(r'/Users/bhtun/summer projects/snake/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load(r'/Users/bhtun/summer projects/snake/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load(r'/Users/bhtun/summer projects/snake/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load(r'/Users/bhtun/summer projects/snake/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load(r'/Users/bhtun/summer projects/snake/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load(r'/Users/bhtun/summer projects/snake/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load(r'/Users/bhtun/summer projects/snake/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load(r'/Users/bhtun/summer projects/snake/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load(r'/Users/bhtun/summer projects/snake/body_bl.png').convert_alpha()
        self.crunch_sound = pygame.mixer.Sound(r'/Users/bhtun/summer projects/snake/crunch.wav')



    def draw_snake(self):
            self.update_head_graphics()
            self.update_tail_graphics()

            for index,block in enumerate(self.body):
                x_pos = int(block.x * cell_size)
                y_pos = int(block.y * cell_size)
                block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)

                if index == 0:
                    screen.blit(self.head,block_rect)
                elif index == len(self.body) - 1:
                    screen.blit(self.tail,block_rect)
                else:
                    previous_block = self.body[index + 1] - block
                    next_block = self.body[index - 1] - block
                    if previous_block.x == next_block.x:
                        screen.blit(self.body_vertical,block_rect)
                    elif previous_block.y == next_block.y:
                        screen.blit(self.body_horizontal,block_rect)
                    else:
                        if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                            screen.blit(self.body_tl,block_rect)
                        elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                            screen.blit(self.body_bl,block_rect)
                        elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                            screen.blit(self.body_tr,block_rect)
                        elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                            screen.blit(self.body_br,block_rect)
    
    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1,0): self.head = self.head_left
        elif head_relation == Vector2(-1,0): self.head = self.head_right
        elif head_relation == Vector2(0,1): self.head = self.head_up
        elif head_relation == Vector2(0,-1): self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1,0): self.tail = self.tail_left
        elif tail_relation == Vector2(-1,0): self.tail = self.tail_right
        elif tail_relation == Vector2(0,1): self.tail = self.tail_up
        elif tail_relation == Vector2(0,-1): self.tail = self.tail_down


    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

    def play_crunch_sound(self):
        self.crunch_sound.play()

    def reset(self):
        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direction = Vector2(0,0)

        

class FRUIT:
    def __init__(self):
        self.randomize()
    
    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)
        self.random_number = random.randint(1, 7)
        

    def draw_fruit(self):
        # create rectangle
        # draw rectangle
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        if self.random_number == 1:
            screen.blit(apple,fruit_rect)
        if self.random_number == 2:
            screen.blit(gt, fruit_rect)
        if self.random_number == 3:
            screen.blit(ncstate, fruit_rect)
        if self.random_number == 4:
            screen.blit(bostonc, fruit_rect)
        if self.random_number == 5:
            screen.blit(clemson, fruit_rect)
        if self.random_number == 6:
            screen.blit(miami, fruit_rect)
        if self.random_number == 7:
            screen.blit(wake, fruit_rect)

class MAIN: # contains the logic of the code
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        self.start_time = pygame.time.get_ticks()
        self.timer_font = pygame.font.Font(None, 36)
    
    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
        self.update_high_score()

    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()
        self.draw_high_score()
        self.draw_timer()
    
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
            self.snake.play_crunch_sound()

        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()
        

    def check_fail(self):
        # check if snake is outside of the area
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
        # check if snake hits itself
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
    
    def game_over(self):
        self.snake.reset()
        

    def draw_grass(self):
        grass_color = (123, 175, 212)
        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,grass_color,grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,grass_color,grass_rect)

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)   
        score_surface = game_font.render(score_text,True,(0,0,0))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        apple_rect = apple.get_rect(midright = (score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left,apple_rect.top,apple_rect.width + score_rect.width + 6,apple_rect.height)

        pygame.draw.rect(screen,(255,255,255),bg_rect)
        screen.blit(score_surface, score_rect)
        screen.blit(apple, apple_rect)
        pygame.draw.rect(screen,(0,0,0),bg_rect,2)

    def update_high_score(self):
        global high_score
        current_score = (len(self.snake.body) - 3)
        if current_score > high_score:
            high_score = current_score

    def draw_high_score(self):
        global high_score
        high_score_text = f"High Score: {high_score}"
        score_surface = game_font.render(high_score_text,True,(0,0,0))
        score_x = int(cell_size * cell_number - 400)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        apple_rect = apple.get_rect(midright = (score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left,apple_rect.top,apple_rect.width + score_rect.width + 6,apple_rect.height)

        pygame.draw.rect(screen,(255,255,255),bg_rect)
        screen.blit(score_surface, score_rect)
        screen.blit(appleunc, apple_rect)
        pygame.draw.rect(screen,(0,0,0),bg_rect,2)

    def draw_timer(self):
        elapsed_time = (pygame.time.get_ticks() - self.start_time) // 1000
        timer_text = f"Time: {elapsed_time:.2f}"
        score_surface = game_font.render(timer_text,True,(0,0,0))
        score_x = int(cell_size * cell_number - 80)
        score_y = int(cell_size * cell_number - 770)
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        apple_rect = apple.get_rect(midright = (score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left,apple_rect.top,apple_rect.width + score_rect.width + 6,apple_rect.height)

        pygame.draw.rect(screen,(255,255,255),bg_rect)
        screen.blit(score_surface, score_rect)
        screen.blit(appleunc, apple_rect)
        pygame.draw.rect(screen,(0,0,0),bg_rect,2)
        



pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
high_score = 0
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size,cell_number * cell_size))
clock = pygame.time.Clock()
apple = pygame.image.load(r'/Users/bhtun/summer projects/snake/duke.png').convert_alpha()
clemson = pygame.image.load(r'/Users/bhtun/summer projects/snake/clemson.png').convert_alpha()
miami = pygame.image.load(r'/Users/bhtun/summer projects/snake/miami.png').convert_alpha()
wake = pygame.image.load(r'/Users/bhtun/summer projects/snake/wake.png').convert_alpha()
bostonc = pygame.image.load(r'/Users/bhtun/summer projects/snake/bostonc.png').convert_alpha()
ncstate = pygame.image.load(r'/Users/bhtun/summer projects/snake/ncstate.png').convert_alpha()
gt = pygame.image.load(r'/Users/bhtun/summer projects/snake/gt.png').convert_alpha()

appleunc = pygame.image.load(r'/Users/bhtun/summer projects/snake/unc.png').convert_alpha()
game_font = pygame.font.Font(None, 40)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150) # event is triggered every 150 miliseconds

main_game = MAIN()
while True:
    # draw all our elements
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
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1,0)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1,0)
    screen.fill((102,169,215))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)