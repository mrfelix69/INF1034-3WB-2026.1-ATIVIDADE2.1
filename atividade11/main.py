import pygame, sys
from pygame.locals import QUIT
from pygame import *

init()

clock = time.Clock()
min_time = 0

hero_img = image.load('Hero_Walk_01.png')

curr_frame = 0
hero_walk_list = []

for i in range(4):
    hero_walk_list.append(image.load(f'Hero_Walk_0{i+1}.png'))

run_animation = False

curr_frame_mg = 0
amin_time_mg = 0

megaman_spritesheet = image.load(
    'megaman_spritesheet.png'
)

screen = display.set_mode((1200,700))

while True:

    for ev in event.get():

        if ev.type == QUIT:
            quit()
            sys.exit()
        if ev.type == KEYDOWN:
            if ev.key == K_SPACE:
                run_animation = True


    clock.tick(60)

    dt = clock.get_time()

    min_time += dt

    if min_time > 100:

        curr_frame += 1

        if curr_frame > len(hero_walk_list) - 1:
            curr_frame = 0

        min_time = 0

    amin_time_mg += dt

    if run_animation == True:

        if amin_time_mg > 100:
            curr_frame_mg += 1
            if curr_frame_mg > 4:
                curr_frame_mg = 0
                run_animation = False
            amin_time_mg = 0

    screen.fill((255,255,255))

    screen.blit(hero_walk_list[curr_frame],(0,0))

    #screen.blit(megaman_spritesheet,(200,200),(60 * curr_frame_mg, 0, 60, 60))

    screen.blit(megaman_spritesheet,(200,200),((curr_frame_mg % 5) * 60,(curr_frame_mg // 5) * 60,60,60))

    display.update()