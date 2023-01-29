import math
import random
import pygame
from pygame import mixer
pygame.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("MY SPACE GAME")
icon=pygame.image.load('ufo.png')
background=pygame.image.load('background.png')
mixer.music.load('background.wav')
mixer.music.play(-1)
pygame.display.set_icon(icon)
playering=pygame.image.load('player.png')
playerX=370
playerY=480
player_changeX=0
enemying=[]
enemyX=[]
enemyY=[]
enemy_changeX=[]
enemy_changeY=[]
num_of_enemies=6
for i in range(num_of_enemies):
    enemying.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(50,150))
    enemy_changeX.append(4)
    enemy_changeY.append(40)
bulleting=pygame.image.load('bullet.png')
bulletX=0
bulletY=480
bullet_changeX=0
bullet_changeY=30
bullet_state='ready'
score_value=0
def show_score(x, y):
    screen.blit(score_value,(x, y))
def game_over_text():
    screen.blit(200,250)
def enemy(x,y,i):
    screen.blit(enemying[i],(x,y))
def player(x,y):
    screen.blit(playering,(x,y))
def fire_bullet(x,y):
    global bullet_state
    bullet_state='fire'
    screen.blit(bulleting,(x+16,y+10))
def iscollision(enemyX,enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + ((math.pow(enemyY - bulletY, 2))))
    if distance < 27:
        return True
    else:
        return False
running=True
while running:
    screen.fill((193, 118, 171))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                player_changeX=-10
            elif event.key==pygame.K_RIGHT:
                player_changeX=10
            elif event.key==pygame.K_SPACE:
                if bullet_state=="ready":
                    bulletSound = mixer.Sound("laser.wav")
                    bulletSound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                player_changeX=0
        playerX+=player_changeX
        if playerX<=0:
            playerX=0
        elif playerX>=736:
            playerX=736
        for i in range(num_of_enemies):
            if enemyY[i]>440:
                for j in range(num_of_enemies):
                    enemyY[j]=2000
                game_over_text()
                break
            enemyX[i]+=enemy_changeX[i]
            if enemyX[i]<=0:
                enemy_changeX[i]=5
                enemyY[i]+=enemy_changeY[i]
            elif enemyX[i]>=736:
                enemy_changeX[i]=-5
                enemyY[i]+=enemy_changeY[i]
            collission = iscollision(enemyX[i],enemyY[i], bulletX, bulletY)
            if collission:
                explosionsound=mixer.Sound('explosion.wav')
                explosionsound.play()
                bulletY = 480
                bullet_state='ready'
                score_value+=1
                enemyX[i]=random.randint(0,736)
                enemyY[i]=random.randint(50,150)
            enemy(enemyX[i],enemyY[i],i)
        if bulletY<=0:
            bulletY=480
            bullet_state='ready'
        if bullet_state=='fire':
            fire_bullet(bulletX, bulletY)
            bulletY-= bullet_changeY
        player(playerX,playerY)
        pygame.display.update()