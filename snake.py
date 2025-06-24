import pygame
import sys
import random

global Score
RIGHT = (20,0)
LEFT = (-20,0)
UP = (0,-20)
DOWN = (0,20)

pygame.init()
screen = pygame.display.set_mode((1280, 720))

Score = 1

Direction = (0,0)
Running = True
Player = [[640,360]]

Apple = [0,0]

pygame.display.set_caption("Catapillar")
def EndGame():
    global Score
    DisplayText(f"YOU GOT {Score} POINTS")
    pygame.time.wait(3000)
    sys.exit(0)


def DisplayText(s):
    font = pygame.font.SysFont("timesnewroman",20)
    thing = font.render(s,True,"Black", "Red")
    screen.blit(thing,(640,360))
    pygame.display.update()

def DrawPlayer():
    global Score
    pygame.draw.rect(screen,(255,0,0), (0 + Player[0][0], 0+ Player[0][1],20,20))
    for i in range(1,Score):
        pygame.draw.rect(screen,(0, 255,0), (0+Player[i][0],0+Player[i][1],20,20))

def DrawApple():
    pygame.draw.rect(screen,"Yellow",(Apple[0],Apple[1],20,20))

def RandApple():
    x = random.randint(0,63)*20
    y = random.randint(0,35)*20
    Apple[0] = x
    Apple[1] = y

RandApple()

def UpdatePlayer():
    global Score
    temp = Player[0]
    Take = None
    Player[0] = [Player[0][0] + Direction[0], Player[0][1] + Direction[1]]

    if Player[0][0] < 0:
        EndGame()
    elif Player[0][0] > 1260:
        EndGame()
    
    if Player[0][1] < 0:
        EndGame()
    elif Player[0][1] > 700:
        EndGame()


    print(Player[0])
    if Score > 1:
        for i in range(1,Score):
            if Player[0] == Player[i]:
                EndGame()
            Take = Player[i]
            if Player[i] == temp:
                continue
            Player[i] = temp
            temp = Take

    if Player[0] == Apple:
        GetPoint()
        RandApple()

def GetPoint():
    global Score
    # very obnoxious setting
    # if random.randint(1,10) == 5:
    #     DisplayText("Uhhhh what the sigma")    
    # else:
    #     DisplayText("You got an apple")
    # MAKE THEM WAIT
    # pygame.time.wait(1000)
    Score += 1
    Player.append(Player[-1])

screen.fill("Blue")

UpdatePlayer()
DrawPlayer()
DrawApple()
pygame.display.update()
pygame.display.flip()

while Running:
    screen.fill("Blue")
    ev = pygame.event.get()
    didKey = False
    tempDir = Direction
    for event in ev:
        if event.type == pygame.QUIT:
            Running = False
        if event.type == pygame.KEYDOWN:
            key = event.key

            if key == pygame.K_UP:
                if Direction != UP and Direction != DOWN:
                    if didKey and tempDir == DOWN:
                        continue
                    Direction = UP
                    didKey = True


            elif key == pygame.K_LEFT:
                if Direction != LEFT and Direction != RIGHT:
                    if didKey and tempDir == RIGHT:
                        continue
                    Direction = LEFT
                    didKey = True

            elif key == pygame.K_DOWN:
                if Direction != UP and Direction != DOWN:
                    if didKey and tempDir == UP:
                        continue
                    Direction = DOWN
                    didKey = True


            elif key == pygame.K_RIGHT:
                if Direction != LEFT and Direction != RIGHT:
                    if didKey and tempDir == LEFT:
                        continue
                    Direction = RIGHT
                    didKey = True

            if key == pygame.K_SPACE:
                GetPoint()

    
    UpdatePlayer()
    DrawPlayer()
    DrawApple()
    pygame.display.update()
    pygame.display.flip()
    pygame.time.wait(60)
