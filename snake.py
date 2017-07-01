import pygame
import sys
import random
import time

check_errors = pygame.init()
if check_errors[1] > 0:
    print("(!) Had" + check_errors[1] + "errors")
    sys.exit(-1)
else:
    print("PyGame initialized ......")

GameWindow = pygame.display.set_mode((720, 460))
pygame.display.set_caption('snake game')

green = pygame.Color(37, 114, 46)
red = pygame.Color(160, 0, 0)
blue = pygame.Color(27, 81, 155)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
brown = pygame.Color(164, 115, 42)

FpsController = pygame.time.Clock()

SnakePos = [100, 50]
SnakeBody = [[100, 50], [90, 50], [80, 50]]

PowerPos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
PowerSpawn = True

score = 0

direction = 'RIGHT'
changeto = direction


def gameOver():
    Font = pygame.font.SysFont('calibre', 72)
    GOsurf = Font.render('Game Over D:', True, black)
    GOrect = GOsurf.get_rect()
    GOrect.midtop = (360, 15)
    GameWindow.blit(GOsurf, GOrect)
    pygame.display.flip()
    ShowScore(0)
    time.sleep(4)
    pygame.quit()
    sys.exit()


def ShowScore(choice = 1):
    ScoreFont = pygame.font.SysFont('calibre', 24)
    ScoreSurf = ScoreFont.render('Score: {0}'.format(score), True, black)
    Srect = ScoreSurf.get_rect()
    if choice == 1:
        Srect.midtop = (80, 10)
    else:
        Srect.midtop = (360, 90)

    GameWindow.blit(ScoreSurf, Srect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('l'):
                changeto = 'RIGHT'
            if event.key == pygame.K_UP or event.key == ord('k'):
                changeto = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('j'):
                changeto = 'DOWN'
            if event.key == pygame.K_LEFT or event.key == ord('h'):
                changeto = 'LEFT'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    if changeto == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if changeto == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if changeto == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if changeto == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'

    if direction == 'RIGHT':
        SnakePos[0] += 10
    if direction == 'LEFT':
        SnakePos[0] -= 10
    if direction == 'UP':
        SnakePos[1] -= 10
    if direction == 'DOWN':
        SnakePos[1] += 10

    SnakeBody.insert(0, list(SnakePos))

    if SnakePos[0] == PowerPos[0] and SnakePos[1] == PowerPos[1]:
        score += 1
        PowerSpawn = False
    else:
        SnakeBody.pop()

    if PowerSpawn == False:
        PowerPos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
    PowerSpawn = True

    GameWindow.fill(white)
    for pos in SnakeBody:
        pygame.draw.rect(GameWindow, green, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(GameWindow, red, pygame.Rect(PowerPos[0], PowerPos[1], 10, 10))

    if SnakePos[0] > 710 or SnakePos[0] < 0:
        gameOver()
    if SnakePos[1] > 450 or SnakePos[1] < 0:
        gameOver()

    for block in SnakeBody[1:]:
        if SnakePos[0] == block[0] and SnakePos[1] == block[1]:
            gameOver()

    pygame.display.flip()
    ShowScore()
    FpsController.tick(25)

