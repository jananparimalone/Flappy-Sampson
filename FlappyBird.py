#Janan Pari Malone
#Flappy Bird

import pygame
import sys
import random

def game_floor():
    screen.blit(floor_base,(floor_x_pos,900))
    screen.blit(floor_base,(floor_x_pos + 576,900))

def check_collision(pipes):
    for bottom_pipe, top_pipe in pipes:
        if bird_rect.colliderect(bottom_pipe) or bird_rect.colliderect(top_pipe):
            die_sound.play()
            return False
    if bird_rect.top <= -100 or bird_rect.bottom >= 900:
        die_sound.play()
        print("HIT Floor")
        return False
    return True

def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop=(700, random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom=(700, random_pipe_pos - 300))
    return bottom_pipe, top_pipe


def move_pipes(pipes):
    for bottom_pipe, top_pipe in pipes:
        bottom_pipe.centerx -= 5
        top_pipe.centerx -= 5
    return pipes

    return pipes
def draw_pipes(pipes):
    for bottom_pipe, top_pipe in pipes:
        screen.blit(pipe_surface, bottom_pipe)
        flip_pipe = pygame.transform.flip(pipe_surface, False, True)
        screen.blit(flip_pipe, top_pipe)


pygame.init()
clock = pygame.time.Clock()

#vars
gravity = 0.25
bird_movement = 0
screen = pygame.display.set_mode((576,1024))

#Download assets from repo and change file path to new location
background = pygame.image.load(r"C:\Users\Janan\Downloads\flappy-bird-assets-master\sprites\background-day.png").convert()
background = pygame.transform.scale2x(background)

#Download assets from repo and change file path to new location
bird = pygame.image.load(r"C:\Users\Janan\Downloads\flappy-bird-assets-master\sprites\IMG_0047.png").convert_alpha()
bird = pygame.transform.scale2x(bird)
bird_rect = bird.get_rect(center = (100,512))

#Download assets from repo and change file path to new location
floor_base = pygame.image.load(r"C:\Users\Janan\Downloads\flappy-bird-assets-master\sprites\base.png").convert()
floor_base = pygame.transform.scale2x(floor_base)
floor_x_pos = 0

#Download assets from repo and change file path to new location
message = pygame.image.load(r"C:\Users\Janan\Downloads\flappy-bird-assets-master\sprites\message.png").convert_alpha()
message = pygame.transform.scale2x(message)
game_over_rect = message.get_rect(center=(288,512))

#Download assets from repo and change file path to new location
pipe_surface = pygame.image.load(r"C:\Users\Janan\Downloads\flappy-bird-assets-master\sprites\pipe-green.png")
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
pipe_height = [400,600,800]
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE,1200)

#Download assets from repo and change file path to new location
flap_sound = pygame.mixer.Sound(r"C:\Users\Janan\Downloads\flappy-bird-assets-master\audio\wing.wav")
die_sound = pygame.mixer.Sound(r"C:\Users\Janan\Downloads\flappy-bird-assets-master\audio\die.wav")

game_active = True

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement -= 12
                flap_sound.play()
            if event.key == pygame.K_SPACE and game_active == False:
                bird_rect.center = (100,512)
                bird_movement = 0
                pipe_list.clear()
                game_active = True
        if event.type == SPAWNPIPE and game_active:
            pipe_list.append(create_pipe())  # Append the tuple to the list
            print(pipe_list)

    screen.blit(background,( 0,0))
    if game_active:
        bird_movement += gravity
        bird_rect.centery += bird_movement
        screen.blit(bird, bird_rect)

        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)

        game_active = check_collision(pipe_list)
    else:
        screen.blit(message, game_over_rect)

    #Create the floor
    floor_x_pos -= 1
    game_floor()
    
    if floor_x_pos <= -576:
        floor_x_pos = 0
    pygame.display.update()
    clock.tick(120)
