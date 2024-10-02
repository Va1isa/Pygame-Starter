import pygame
from src.constants import *

pygame.init()
screen = pygame.display.set_mode(WIN_SIZE, pygame.SCALED)
clock = pygame.time.Clock()

player_image = pygame.image.load("assets/players.png").convert_alpha()
player_rect = player_image.get_frect()
player_direction = pygame.Vector2()
player_speed = 50


running = True
while running:
    dt = clock.tick(60) / 1000
    keys = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


            player_direction.xy = (0,0)
            if keys[pygame.K_w]:
                player_direction.y -= 1
            if keys[pygame.K_s]:
                player_direction.y += 1
            if keys[pygame.K_a]:
                player_direction.x -= 1
            if keys[pygame.K_d]:
                player_direction.x += 1

            if player_direction:
                player_direction.normalize_ip()
            player_rect.center += player_direction * player_speed * dt

            screen.fill("black")
            screen.blit(player_image, player_rect)
    
    pygame.display.flip()
