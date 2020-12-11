import FileRead
import math
import pygame as pg
import time

FILENAME = "input.txt"
F = FileRead.ReadInput(FILENAME)

VISUALIZE = input("Want to see an animation? y/n: ").upper() == "y".upper()
SCALE = 20
DOTSIZE = 5
def initVisual():
    pg.init()
    temp = FileRead.ReadInput(FILENAME)
    print(len(temp[0]), len(temp))
    size = [len(temp[0]) * SCALE + 20, 40 * SCALE + 50]
    print(size)
    screen = pg.display.set_mode(size)
    screen.fill((0,0,0))
    font = pg.font.Font('freesansbold.ttf', 32)
    return screen, font

offset = 0
start = 0
def visualize(data, coordinate = None, init=False, color = (255,0,0), trees = None):
    global screen, font, offset, start
    if init:
        for i in range(start,start + 40):
            if i >= len(data):
                return None
            for x in range(0,len(data[i])):
                if data[i][x] == "#":
                    color = (0,255,0)
                else:
                    color = (75,75,75)
                c = [x,i]
                pg.draw.circle(screen, color, (c[0] * SCALE + 10, c[1] * SCALE + 10), DOTSIZE)
    elif coordinate:
        if coordinate[1] >= start + 40:
            screen.fill((0,0,0))
            start = start + 40
            offset -= 40
            for i in range(start,start + 40):
                if i >= len(data):
                    return None
                for x in range(0,len(data[i])):
                    if data[i][x] == "#":
                        color = (0,255,0)
                    else:
                        color = (75,75,75)
                    c = [x, i + offset]
                    pg.draw.circle(screen, color, (c[0] * SCALE + 10, c[1] * SCALE + 10), DOTSIZE)
        pg.draw.circle(screen, color,
                ((coordinate[0])* SCALE + 10, (coordinate[1] + offset) * SCALE + 10), DOTSIZE)
    if trees is not None:
        text = font.render(str(trees), True, (255,0,0), (0,0,0))
        textRect = text.get_rect()
        w,h = pg.display.get_surface().get_size()
        textRect.center = (50,h-10)
        pg.draw.rect(screen, (0,0,0), (0,h-50,100,h))
        screen.blit(text, textRect)
    pg.display.flip()
    time.sleep(1/30)

def isTree(Char):
    return True if Char == "#" else False

def traverse(Slope): #[X, Y] slope
    X = 0
    Y = 0
    Trees = 0
    for i in range(0, len(F), Slope[1]):
        Line = F[i]
        if X >= len(Line):
            if VISUALIZE:
                visualize(F, init = True)
            X = X % len(Line)
        if isTree(Line[X]):
            Trees += 1
            if VISUALIZE:
                visualize(F, (X,Y), color = (255,0,0), trees = Trees)
        else:
            if VISUALIZE:
                visualize(F, (X,Y), color = (0,0,255), trees = Trees)
        Y += Slope[1]
        X += Slope[0]
    return Trees

def solution1():
    Answer = traverse([3, 1])
    print("Trees for slope 3,1 is: {}".format(Answer))

def solution2():
    global offset, start
    Slopes = [
                [1,1],
                [3,1],
                [5,1],
                [7,1],
                [1,2]
            ]
    Answers = []
    for Slope in Slopes:
        if VISUALIZE:
            offset = 0
            start = 0
            visualize(F, init = True)
        Answers.append(traverse(Slope))
        if VISUALIZE:
            input(str(Answers[-1]) + " continue")

    print("Product of all slopes is: {}".format(math.prod(Answers)))

if VISUALIZE:
    screen, font = initVisual()
    visualize(F, init = True)

solution1()
if VISUALIZE:
    input("continue")
solution2()
