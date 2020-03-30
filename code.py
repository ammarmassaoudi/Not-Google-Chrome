import pygame
from pygame.locals import *
import os
import sys
import math
import random


pygame.init()


bg1_x = 0
bg2_x = 0
bg3_x = 0


L = 710
W = 386
velocity = 10
speed = 27

score = -1


win = pygame.display.set_mode((L, W))
pygame.display.set_caption("Not Google Chrome")


walkRight = [pygame.image.load('images/R1.png'), pygame.image.load('images/R2.png'), pygame.image.load('images/R3.png'), pygame.image.load('images/R4.png'), pygame.image.load(
    'images/R5.png'), pygame.image.load('images/R6.png'), pygame.image.load('images/R7.png'), pygame.image.load('images/R8.png'), pygame.image.load('images/R9.png'), pygame.image.load('images/R10.png'), pygame.image.load('images/R11.png'), pygame.image.load('images/R12.png'), pygame.image.load('images/R13.png'), pygame.image.load(
    'images/R14.png'), pygame.image.load('images/R15.png'), pygame.image.load('images/R16.png'), pygame.image.load('images/R17.png'), pygame.image.load('images/R18.png')]

jumping = [pygame.image.load('images/J1.png'), pygame.image.load('images/J2.png'), pygame.image.load('images/J3.png'), pygame.image.load('images/J4.png'), pygame.image.load(
    'images/J5.png'), pygame.image.load('images/J6.png'), pygame.image.load('images/J7.png'), pygame.image.load('images/J8.png'), pygame.image.load('images/J9.png')]

sliding = [pygame.image.load('images/S1.png'), pygame.image.load('images/S2.png'), pygame.image.load('images/S3.png'), pygame.image.load('images/S4.png'), pygame.image.load(
    'images/S5.png'), pygame.image.load('images/S6.png'), pygame.image.load('images/S7.png'), pygame.image.load('images/S8.png'), pygame.image.load('images/S9.png')]
bg = pygame.image.load('images/endscreen.png')
bg1 = pygame.image.load('images/bg1.png')
bg2 = pygame.image.load('images/bg2.png')
bg3 = pygame.image.load('images/bg3.png')
bg_s = pygame.image.load('images/start.png')
clock = pygame.time.Clock()


class player(object):
    def __init__(self, x, y, width, height):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.walkCount = 0
        self.right = True
        self.isSliding = False
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if self.right:
            win.blit(walkRight[self.walkCount//2], (self.x+50, self.y+10))
            self.walkCount += 1

        elif self.isJump:
            win.blit(jumping[self.walkCount//3], (self.x+50, self.y+10))
            self.walkCount += 1

        elif self.isSliding:
            win.blit(sliding[self.walkCount//3], (self.x+40, self.y+10))
            self.walkCount += 1
        if man.isSliding == True:
            self.hitbox = (self.x+40, self.y+80, 110, 64)

            # uncomment to see the hitbox :
            # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        else:
            self.hitbox = (self.x+80, self.y+30, 64, 110)
            # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)


class enemy(object):

    walkLeft = [pygame.image.load('images/L1E.png'), pygame.image.load('images/L2E.png'), pygame.image.load('images/L3E.png'), pygame.image.load('images/L4E.png'), pygame.image.load('images/L5E.png'), pygame.image.load(
        'images/L6E.png'), pygame.image.load('images/L7E.png'), pygame.image.load('images/L8E.png'), pygame.image.load('images/L9E.png'), pygame.image.load('images/L10E.png'), pygame.image.load('images/L11E.png')]
    enemy = pygame.image.load('images/L1E.png')

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.walkCount = 0
        self.vel = 13
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def draw(self, win):
        e_x = self.x+220
        e_y = self.y+30

        if self.walkCount >= 27:
            self.walkCount = 0
        win.blit(pygame.transform.scale(
            self.walkLeft[self.walkCount//3], (128, 128)), (e_x, e_y))
        self.walkCount += 1

        self.hitbox = (self.x+260, self.y+35, 45, 110)

        # uncomment to see the hitbox :
        #pygame.draw.rect(win, (0, 0, 0), self.hitbox, 2)

    def collide(self, rect):
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] + rect[3] > self.hitbox[1]:
                return True
        return False


class enemy2(object):

    flyLeft = [pygame.image.load('images/E1.png'), pygame.image.load('images/E2.png'), pygame.image.load('images/E3.png'), pygame.image.load(
        'images/E4.png'), pygame.image.load('images/E5.png'), pygame.image.load('images/E6.png'), pygame.image.load('images/E7.png'), pygame.image.load('images/E8.png'), pygame.image.load('images/E9.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.walkCount = 0
        self.vel = 13
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def draw(self, win):

        e_x = self.x+265
        e_y = self.y+20
        e_y2 = self.y-50
        if self.walkCount >= 27:
            self.walkCount = 0
        win.blit(pygame.transform.scale(
            self.flyLeft[self.walkCount//3], (60, 60)), (e_x, e_y2))

        win.blit(pygame.transform.scale(
            self.flyLeft[self.walkCount//3], (60, 60)), (e_x, e_y))
        self.walkCount += 1

        self.hitbox = (self.x+270, self.y+30, 50, 40)

        # uncomment to see the hitbox :
        #pygame.draw.rect(win, (0, 0, 0), self.hitbox, 2)

    def collide(self, rect):

        if rect[0] + rect[2] > self.hitbox[0] and rect[1] < self.hitbox[1] + self.hitbox[3]:
            if rect[0] < self.hitbox[0]+self.hitbox[2]:
                return True
            return False


def redrawGameWindow():

    win.blit(bg3, (bg3_x, 0))
    win.blit(bg2, (bg2_x, 0))
    win.blit(bg1, (bg1_x, 0))

    man.draw(win)

    for obstacle in obstacles:
        obstacle.draw(win)
        man.y == 230
        if obstacle.collide(man.hitbox):
            endScreen()
    # drawing the score:
    FONT = pygame.font.SysFont("lucidaconsole", 30)
    if score == -1:
        win.blit(FONT.render('score : 0',
                             True, (255, 255, 255), (0, 0, 0)), (260, 40))
        pygame.display.update()
    else:
        win.blit(FONT.render('score : ' + str(score),
                             True, (255, 255, 255), (0, 0, 0)), (260, 40))
        pygame.display.update()
    finalscore = str(score)
    pygame.display.update()


def endScreen():
    global pause, score, speed, obstacles
    pause = 0
    speed = 30
    obstacles = []
    man.jumpCount == 0

    # another game loop
    end = True
    while end:
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                # quit()

        # display the final score:
        bigFont = pygame.font.SysFont("lucidaconsole", 60)
        win.blit(bg, (0, 0))

        youdied = bigFont.render(
            'you died lol', 1, (255, 255, 255), (0, 0, 0))
        currentScore = bigFont.render(
            'Your score : ' + finalscore, 1, (255, 255, 255), (0, 0, 0))
        win.blit(youdied, (W/2-50, 40))
        win.blit(currentScore, (115, 150))
        button3 = pygame.image.load('images/button4.png')
        button4 = pygame.image.load('images/button3.png')

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        # print(mouse)
        if 437 > mouse[0] > 277 and 330 > mouse[1] > 270:
            win.blit(button3, (277, 270))
            if click[0] == 1:
                man.right = False
                man.isSliding = False
                man.isJump = True
                man.isjump = False
                break

        else:
            win.blit(button4, (277, 270))
        pygame.display.update()
    score = -1


def game_intro():
    intro = True
    while intro:
        win.blit(bg_s, (0, 0))
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                # quit()
        # button:
        button1 = pygame.image.load('images/button1.png')
        button2 = pygame.image.load('images/button2.png')

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if 280+150 > mouse[0] > 280 and 190+60 > mouse[1] > 190:
            win.blit(button2, (280, 190))
            if click[0] == 1:
                intro = False
        else:
            win.blit(button1, (280, 190))
        pygame.display.update()
        clock.tick(27)


game_intro()


run = True
man = player(-20, 230, 64, 64)
wa7ch = enemy(400, 230, 64, 64, 300)
ferkh = enemy2(400, 230, 64, 64, 300)

obstacles = []
score = -1
pygame.time.set_timer(USEREVENT+2, random.randrange(2000, 3000))
pygame.time.set_timer(USEREVENT+1, 500)


while run:

    clock.tick(speed)

    bg1_x -= 6
    if bg1_x < -710:
        bg1_x = 0

    bg2_x -= 5
    if bg2_x < -710:
        bg2_x = 0

    bg3_x -= 3
    if bg3_x < -710:
        bg3_x = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            # quit()
        if event.type == USEREVENT+1:
            speed += 0.3

        if event.type == USEREVENT+2:
            r = random.randrange(0, 2)

            if r == 0:
                obstacles.append(enemy(400, 230, 64, 64, 300))
                score += 1
            elif r == 1:
                obstacles.append(enemy2(400, 230, 64, 64, 300))
                score += 1

    # drawing enemies :
    for obstacle in obstacles:

        obstacle.x -= velocity

        if obstacle.x < -710:

            obstacles.pop(obstacles.index(obstacle))
            velocity += 0.3

    keys = pygame.key.get_pressed()

    if keys[pygame.K_DOWN]:
        man.isSliding = True
        man.right = False

    else:
        man.right = True
        man.isSliding = False

    if not(man.isJump):
        if keys[pygame.K_SPACE]:
            man.isJump = True
            man.right = False
            man.walkCount = 0

    else:
        if man.jumpCount >= -10:
            man.y -= (man.jumpCount * abs(man.jumpCount)) * 0.55
            man.jumpCount -= 1
            man.right = False
        else:
            man.jumpCount = 10
            man.isJump = False
            man.right = True

    redrawGameWindow()
    finalscore = str(score)

pygame.quit()
