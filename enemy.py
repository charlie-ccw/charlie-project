import pygame
from random import *

 # here we difine the smallest enemy plane
class Enemy1(pygame.sprite.Sprite):
    def __init__(self,size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/6.png").convert_alpha()
        # here we difine the destory picture of the enemy
        self.destroy_images = []
        self.destroy_images.extend([\
             pygame.image.load("images/7.png").convert_alpha(),\
             pygame.image.load("images/8.png").convert_alpha(),\
             pygame.image.load("images/9.png").convert_alpha(),\
             pygame.image.load("images/1.png").convert_alpha(),\
             ])
        self.rect = self.image.get_rect()
        self.width = 700
        self.height = 960
        self.speed = 5
        # here we set the condition of the picture
        self.active = True
        self.rect.left = randint(0,self.width - self.rect.width)
        self.rect.bottom = randint(self.height*-5,0)
        self.mask = pygame.mask.from_surface(self.image)


     # here we difine the movemont of the enemy
    def move(self):
        if self.rect.top < self.height:
            self.rect.top +=self.speed
        else:
            self.reset()

     # here we define how the enemy reset in the game
    def reset(self):
        self.active = True
        self.rect.left = randint(0,self.width - self.rect.width)
        self.rect.bottom = randint(self.height*-5,0)
        





 # here we difine the middle size enemy plane
class Enemy2(pygame.sprite.Sprite):
    def __init__(self,size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/14.png").convert_alpha()
        # here we difine the destory picture of the enemy
        self.destroy_images = []
        self.destroy_images.extend([\
             pygame.image.load("images/15.png").convert_alpha(),\
             pygame.image.load("images/16.png").convert_alpha(),\
             pygame.image.load("images/17.png").convert_alpha(),\
             pygame.image.load("images/1.png").convert_alpha(),\
             ])
        self.rect = self.image.get_rect()
        self.width = 700
        self.height = 960
        self.speed = 2
        # here we set the condition of the picture
        self.active = True
        self.rect.left = randint(0,self.width - self.rect.width)
        self.rect.bottom = randint(self.height*-10,-self.height)
        self.mask = pygame.mask.from_surface(self.image)


     # here we difine the movemont of the enemy
    def move(self):
        if self.rect.top < self.height:
            self.rect.top +=self.speed
        else:
            self.reset()

     # here we define how the enemy reset in the game
    def reset(self):
        self.active = True
        self.rect.left = randint(0,self.width - self.rect.width)
        self.rect.bottom = randint(self.height*-10,0)





 # here we difine the biggest size enemy plane
class Enemy3(pygame.sprite.Sprite):
    def __init__(self,size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/2.png").convert_alpha()
        # here we difine the destory picture of the enemy
        self.destroy_images = []
        self.destroy_images.extend([\
             pygame.image.load("images/3.png").convert_alpha(),\
             pygame.image.load("images/4.png").convert_alpha(),\
             pygame.image.load("images/5.png").convert_alpha(),\
             pygame.image.load("images/1.png").convert_alpha(),\
             ])
        self.rect = self.image.get_rect()
        self.width = 700
        self.height = 960
        self.speed = 1
        # here we set the condition of the picture
        self.active = True
        self.rect.left = randint(0,self.width - self.rect.width)
        self.rect.bottom = randint(self.height*-12,-self.height*2)
        self.mask = pygame.mask.from_surface(self.image)


     # here we difine the movemont of the enemy
    def move(self):
        if self.rect.top < self.height:
            self.rect.top +=self.speed
        else:
            self.reset()

     # here we define how the enemy reset in the game
    def reset(self):
        self.active = True
        self.rect.left = randint(0,self.width - self.rect.width)
        self.rect.bottom = randint(self.height*-10,0)
