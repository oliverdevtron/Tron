from turtle import *
from freegames import square, vector
import pygame

# Initialize pygame mixer for sound effects
pygame.mixer.init()
collision_sound = pygame.mixer.Sound('collision.mp3')
win_sound = pygame.mixer.Sound('win.mp3')

# Größeres Spielfeld
field_size = 300

xy1 = vector(-150, 0)
aim1 = vector(4, 0)
body1 = set()

xy2 = vector(150, 0)
aim2 = vector(-4, 0)
body2 = set()

def inside(head):
    return -field_size < head.x < field_size and -field_size < head.y < field_size

def draw():
    xy1.move(aim1)
    head1 = xy1.copy()
    xy2.move(aim2)
    head2 = xy2.copy()

    if not inside(head1) or head1 in body2:
        win_sound.play()
        print('Blue Player Wins!')
        ontimer(reset_game, 2000)
        return

    if not inside(head2) or head2 in body1:
        win_sound.play()
        print('Red Player Wins!')
        ontimer(reset_game, 2000)
        return

    body1.add(head1)
    body2.add(head2)
    square(xy1.x, xy1.y, 10, 'red')
    square(xy2.x, xy2.y, 10, 'blue')
    update()
    ontimer(draw, 50)

def reset_game():
    global xy1, aim1, body1, xy2, aim2, body2
    xy1 = vector(-150, 0)
    aim1 = vector(4, 0)
    body1 = set()

    xy2 = vector(150, 0)
    aim2 = vector(-4, 0)
    body2 = set()
    clear()
    draw()

def change_direction(player, direction):
    if player == 1:
        if direction == 'up' and aim1 != vector(0, -4):
            aim1.x, aim1.y = 0, 4
        elif direction == 'down' and aim1 != vector(0, 4):
            aim1.x, aim1.y = 0, -4
        elif direction == 'left' and aim1 != vector(4, 0):
            aim1.x, aim1.y = -4, 0
        elif direction == 'right' and aim1 != vector(-4, 0):
            aim1.x, aim1.y = 4, 0
    elif player == 2:
        if direction == 'up' and aim2 != vector(0, -4):
            aim2.x, aim2.y = 0, 4
        elif direction == 'down' and aim2 != vector(0, 4):
            aim2.x, aim2.y = 0, -4
        elif direction == 'left' and aim2 != vector(4, 0):
            aim2.x, aim2.y = -4, 0
        elif direction == 'right' and aim2 != vector(-4, 0):
            aim2.x, aim2.y = 4, 0

def play_collision_sound():
    collision_sound.play()

setup(700, 700, 370, 0)  # Vergrößertes Spielfeld
bgcolor('lightgreen')
title("Tron für Kinder")
hideturtle()
tracer(False)
listen()
onkey(lambda: change_direction(1, 'up'), 'w')
onkey(lambda: change_direction(1, 'down'), 's')
onkey(lambda: change_direction(1, 'left'), 'a')
onkey(lambda: change_direction(1, 'right'), 'd')
onkey(lambda: change_direction(2, 'up'), 'i')
onkey(lambda: change_direction(2, 'down'), 'k')
onkey(lambda: change_direction(2, 'left'), 'j')
onkey(lambda: change_direction(2, 'right'), 'l')
draw()
done()
