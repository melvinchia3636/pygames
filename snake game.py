import pygame
import random

pygame.init()

clock = pygame.time.Clock()

win_length = 500
win_height = 500
vel = 10

direction='DOWN'

win = pygame.display.set_mode((win_length, win_height))

pygame.display.set_caption('Snake Game')

white = 255, 255, 255

snakehead = [240,240]
food = [int((random.randint(0,win_length))/10)*10, int((random.randint(0,win_height))/10)*10]
snake_pos = [[240,240],[240,230],[240,220]]
r = 10
g = 10
b = 10

def draw_snake():
    global r, g, b
    win.fill((0,0,0))

    r+=10
    g+=10
    b+=10
    if r>255:
        r=10
    if g>255:
        g=10
    if b>255:
        b=10
        
    for position in snake_pos:
        pygame.draw.rect(win, (r, g, b), pygame.Rect(position[0], position[1], 10, 10))
    
def show_food():

    global food
    
    pygame.draw.rect(win, (0, 255, 0), pygame.Rect(food[0], food[1], 10, 10))

    if snakehead==food:
        food = [int((random.randint(0,win_length))/10)*10, int((random.randint(0,win_height))/10)*10]
        snake_pos.append(food)

def detect_move():

    global direction
    global snakehead
    global snake_pos
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        direction = 'LEFT'

    if keys[pygame.K_RIGHT]:
        direction = 'RIGHT'

    if keys[pygame.K_UP]:
        direction = 'UP'

    if keys[pygame.K_DOWN]:
        direction = 'DOWN'

    if direction=='DOWN':
        snakehead[1] += vel
        snake_pos.insert(0,list(snakehead))
        snake_pos.pop()

    if direction=='UP':
        snakehead[1] -= vel
        snake_pos.insert(0,list(snakehead))
        snake_pos.pop()

    if direction=='LEFT':
        snakehead[0] -= vel
        snake_pos.insert(0,list(snakehead))
        snake_pos.pop()

    if direction=='RIGHT':
        snakehead[0] += vel
        snake_pos.insert(0,list(snakehead))
        snake_pos.pop()

run = True

while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    detect_move()
    draw_snake()
    show_food()
    pygame.display.update()
    print(snakehead[0],snakehead[1])

    clock.tick(15)

pygame.quit()
