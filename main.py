#Feel free to use parts of the code below in your final project!

#The code below is for generating map5 as seen in the Maps folder in the Final Project Scaffold. You can edit it to your own liking!

import pygame, sys, time
from pygame import mixer
from pygame.locals import *
from settings import *
from spritesheet import *

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('    Moonlight Valley')

from player import *
from giant_slime import *
from slime import *
from small_slime import *

clock = pygame.time.Clock()
frame = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 150

pygame.font.init()
MAIN_MENU_FONT = pygame.font.Font('svcaps.ttf', 75)
PLAY_FONT = pygame.font.Font('alagard.ttf', 72)
CREDITS_FONT = pygame.font.Font('alagard.ttf', 40)
SMALL_CREDITS_FONT = pygame.font.Font('alagard.ttf', 20)
DEATH_FONT = pygame.font.Font('alagard.ttf', 112)

mixer.music.load('01 Stardew.mp3')
mixer.music.set_volume(0.2)
mixer.music.play()
attack_sound = pygame.mixer.Sound('attack.wav')

menu_background = pygame.image.load(
    'sentry_landscape_stardew_valley_inspired_resized.png').convert_alpha()
menu_background = pygame.transform.scale(menu_background,
                                         (SCREEN_WIDTH, SCREEN_HEIGHT))

dirt = pygame.image.load('stardew_things/outside/stardew_path_2.0.webp'
                         ).convert_alpha()  # How the images are loaded in
dirt = pygame.transform.scale(dirt, (48, 48))

grass = pygame.image.load(
    'stardew_things/outside/stardew_grass.webp').convert_alpha(
    )  # How the images are loaded in stardew_things/stardew grass.webp
grass = pygame.transform.scale(grass, (48, 48))

tree_sprite_sheet = pygame.image.load(
    "stardew_things/outside/stardew_trees.png").convert_alpha()
tree_sheet = spritesheet.SpriteSheet(tree_sprite_sheet)
tree_images = []
for i in range(4):
    tree_images.append(tree_sheet.get_image(0, i, 96, 160, 1, (0, 0, 0)))
    tree_images[i] = pygame.transform.scale(tree_images[i].convert_alpha(),
                                            (48, 96))

crops_sprite_sheet = pygame.image.load("crops2.png").convert_alpha()
crops_sheet = spritesheet.SpriteSheet(crops_sprite_sheet)
crop_images = []
for i in range(12):
    crop_images.append(crops_sheet.get_image(0, i, 15, 27, 1, (0, 0, 0)))
    crop_images[i] = pygame.transform.scale(crop_images[i].convert_alpha(),
                                            (23, 42))

#print(crop_images)

crops3_sprite_sheet = pygame.image.load("crops3.png").convert_alpha()
crops3_sheet = spritesheet.SpriteSheet(crops3_sprite_sheet)
crops3_images = []
for i in range(14):
    crops3_images.append(crops3_sheet.get_image(0, i, 15.8, 21, 1, (0, 0, 0)))
    crops3_images[i] = pygame.transform.scale(crops3_images[i].convert_alpha(),
                                              (23, 28))

wall = pygame.image.load(
    "mystic_woods_u/tilesets/walls/brick.jpg").convert_alpha()
wall = pygame.transform.scale(wall, (48, 48))

longWall = pygame.image.load(
    "mystic_woods_u/tilesets/walls/wall1.png").convert_alpha()
longWall = pygame.transform.scale(longWall, (96, 48))

path = pygame.image.load(
    'stardew_things/outside/stardew_path_3.0.webp').convert_alpha()
path = pygame.transform.scale(path, (48, 48))

dandelion = pygame.image.load(
    "stardew_things/outside/dandelion.webp").convert_alpha()
dandelion = pygame.transform.scale(dandelion, (48, 48))

farm = pygame.image.load(
    "stardew_things/outside/stardew_farm.webp").convert_alpha()
farm = pygame.transform.scale(farm, (240, 192))
# Farm entrance is from 360, 60 - 392, 60
# Farm walls are from 307 - 592
# need to build a collidable rect to stop player, except at entrance
wooden_floor = pygame.image.load(
    "stardew_things/inside decor/woodenfloor.webp").convert_alpha()
wooden_floor = pygame.transform.scale(wooden_floor, (48, 48))

brickFirePlace = pygame.image.load(
    "stardew_things/inside decor/brick_fireplace.png").convert_alpha()
brickFirePlace = pygame.transform.scale(brickFirePlace, (48, 96))

bookcase = pygame.image.load(
    "stardew_things/inside decor/bookcase.png").convert_alpha()
bookcase = pygame.transform.scale(bookcase, (48, 96))

bed = pygame.image.load("stardew_things/inside decor/bed.webp").convert_alpha()
bed = pygame.transform.scale(bed, (96, 128))

brownCouch = pygame.image.load(
    "stardew_things/inside decor/browncouch.png").convert_alpha()
brownCouch = pygame.transform.scale(brownCouch, (96, 48))

yellowCouch = pygame.image.load(
    "stardew_things/inside decor/yellowcouch.webp").convert_alpha()
yellowCouch = pygame.transform.scale(yellowCouch, (96, 48))

greenCouch = pygame.image.load(
    "stardew_things/inside decor/greencouch.png").convert_alpha()
greenCouch = pygame.transform.scale(greenCouch, (96, 48))

housePlant = pygame.image.load(
    "stardew_things/inside decor/house_plant.webp").convert_alpha()
housePlant = pygame.transform.scale(housePlant, (32, 64))

moonTable = pygame.image.load(
    "stardew_things/inside decor/moontable.png").convert_alpha()
moonTable = pygame.transform.scale(moonTable, (56, 56))

sunTable = pygame.image.load(
    "stardew_things/inside decor/suntable.webp").convert_alpha()
sunTable = pygame.transform.scale(sunTable, (56, 56))

chair = pygame.image.load(
    "stardew_things/inside decor/oakchair.webp").convert_alpha()
chair = pygame.transform.scale(chair, (24, 48))

lamp = pygame.image.load(
    "stardew_things/inside decor/lamp.webp").convert_alpha()
lamp = pygame.transform.scale(lamp, (36, 60))

blossomRug = pygame.image.load(
    "stardew_things/inside decor/blossomrug.png").convert_alpha()
blossomRug = pygame.transform.scale(blossomRug, (96, 48))

cart = pygame.image.load(
    "stardew_things/outside/stardew_cart.webp").convert_alpha()
cart = pygame.transform.scale(cart, (144, 96))

star_floor = pygame.image.load(
    "stardew_things/inside decor/starrug.webp").convert_alpha()
star_floor = pygame.transform.scale(star_floor, (48, 48))

dandelion = pygame.image.load(
    "stardew_things/outside/dandelion.webp").convert_alpha()
dandelion = pygame.transform.scale(dandelion, (20, 20))

fruitRug = pygame.image.load(
    "stardew_things/inside decor/fruit_salad_rug.webp").convert_alpha()
fruitRug = pygame.transform.scale(fruitRug, (74, 56))

oakTable = pygame.image.load(
    "stardew_things/inside decor/oaktable.png").convert_alpha()
oakTable = pygame.transform.scale(oakTable, (34, 42))

tile_size = (48, 48)


def load_map(path):
    '''Function to load the map file and split it into list.

    Inputs:
    path: the folder where the map is stored

    Outputs:
    game_map: the map on the screen
    
    '''
    f = open(path + '.txt', 'r')
    data = f.read()
    f.close
    data = data.split('\n')
    game_map = []
    for row in data:
        game_map.append(list(row))
    return game_map


def draw_text(text, font, color, surface, x, y, angle):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(pygame.transform.rotate(textobj, angle), textrect)


def get_xy_to_center_text(text, font):
    textobj = font.render(text, 1, (0, 0, 0))
    print("X: " + str((SCREEN_WIDTH - textobj.get_rect()[2]) / 2))
    print("Y: " + str((SCREEN_HEIGHT - textobj.get_rect()[3]) / 2))


#Loads map file
game_maps = []
game_maps.append(load_map('Maps/map1'))
game_maps.append(load_map('Maps/map2'))
game_maps.append(load_map('Maps/map3'))

#Opens the map as listed in maps.txt in the Maps folder.

#get_xy_to_center_text("You Died", DEATH_FONT)
#get_xy_to_center_text("Play!", PLAY_FONT)
#get_xy_to_center_text("Chelsea DiBartolo, Lillian Learned, Maureen Reyes, Princess Kromah, Vivian Shao", SMALL_CREDITS_FONT)

player1 = Player()
furniture_hitboxes = [
    pygame.Rect(49, 483, 237, 92),
    pygame.Rect(47, 305, 96, 109),
    pygame.Rect(98, 50, 191, 94),
    pygame.Rect(145, 194, 102, 54),
    pygame.Rect(382, 49, 50, 47),
    pygame.Rect(530, 51, 188, 92),
    pygame.Rect(576, 194, 102, 55),
    pygame.Rect(623, 305, 96, 111),
    pygame.Rect(362, 300, 31, 39),
    pygame.Rect(481, 481, 235, 88)
]
slime1 = Slime()
slime2 = Slime(144)
slime3 = Slime(432)
slime4 = Small_Slime(120)
slime5 = Small_Slime(456)
slimes = [slime1, slime2, slime3, slime4, slime5]
bigslime = Giant_Slime()

click = None
menu = True
in_credits = False
gaming = False
place = 0
while True:
    mixer.music.play()
    # MAIN MENU LOOP
    while menu:
        screen.fill((156, 175, 136))
        screen.blit(menu_background, (0, 0))

        mx, my = pygame.mouse.get_pos()
        # to revert title screen, redraw at ~72 height
        draw_text("Moonlight       Valley", MAIN_MENU_FONT, (255, 255, 255),
                  screen, 35, 35, 0)
        # try an angle of 5 for some spice
        # to revert playbutton W = 300, both buttons shifted right 40
        play_button = pygame.Rect(8, 384, 250, 96)
        credits_button = pygame.Rect(8, 496, 200, 72)

        # can be replaced with
        # screen.blit( pygame.transform.scale("folder/image.jpg", 0.5) , (x, y))
        pygame.draw.rect(screen, (255, 255, 255), play_button, 5, 12)
        pygame.draw.rect(screen, (255, 255, 255), credits_button, 5, 12)

        if play_button.collidepoint((mx, my)):
            pygame.draw.rect(screen, (10, 52, 149), play_button, 0, 12)
            pygame.draw.rect(screen, (255, 255, 255), play_button, 5, 12)
            if click:
                print("Play!")
                gaming = True
                menu = False

        if credits_button.collidepoint((mx, my)):
            pygame.draw.rect(screen, (155, 155, 155), credits_button, 0, 12)
            pygame.draw.rect(screen, (255, 255, 255), credits_button, 5, 12)
            if click:
                print("Credits")
                menu = False
                in_credits = True
        # shift play right 65, credits right 40
        draw_text("Play!", PLAY_FONT, (255, 255, 255), screen, 55, 400, 0)
        draw_text("Credits", CREDITS_FONT, (255, 255, 255), screen, 40, 516, 0)
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(FPS)

    # CREDITS PAGE LOOP
    while in_credits:
        screen.fill((16, 24, 58))

        draw_text(
            "Shout out to https://game-endeavor.itch.io for the core sprite sheets",
            SMALL_CREDITS_FONT, (255, 255, 255), screen, 10, 20, 0)
        draw_text("Also shout out to Hewett Tsoi on DaFont.com",
                  SMALL_CREDITS_FONT, (255, 255, 255), screen, 10, 50, 0)
        draw_text("for creating the Alagard (fantasy) font used throughout",
                  SMALL_CREDITS_FONT, (255, 255, 255), screen, 50, 70, 0)
        draw_text(
            "This game also is heavily inspired by Stardew Valley, both in design and aesthetic.",
            SMALL_CREDITS_FONT, (255, 255, 255), screen, 10, 100, 0)
        draw_text("Menu Art generated by Midjourney AI.", SMALL_CREDITS_FONT,
                  (255, 255, 255), screen, 10, 120, 0)
        draw_text("Finally this game is all thanks to the hard work from",
                  SMALL_CREDITS_FONT, (255, 255, 255), screen, 135.5, 200, 0)
        draw_text(
            "Chelsea DiBartolo, Lillian Learned, Maureen Reyes, Princess Kromah, Vivian Shao",
            SMALL_CREDITS_FONT, (255, 255, 255), screen, 11.5, 220, 0)
        draw_text("and led Project Manager Travis Smalling",
                  SMALL_CREDITS_FONT, (255, 255, 255), screen, 135, 240, 0)

        draw_text("Press ESC to leave", CREDITS_FONT, (255, 255, 255), screen,
                  214, 420, 0)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    menu = True
                    in_credits = False
        pygame.display.update()
        clock.tick(FPS)

    # MAIN GAME LOOP
    while gaming:
        screen.fill((152, 118, 82))  #Sets the sky-blue BG color
        y = 0
        for row in game_maps[place]:
            x = 0
            for tile in row:
                if tile == '1':
                    screen.blit(dirt, (x * tile_size[0], y * tile_size[1]))
                elif tile == '2':
                    screen.blit(grass, (x * tile_size[0], y * tile_size[1]))
                elif tile == '3':
                    screen.blit(path, (x * tile_size[0], y * tile_size[1]))
                elif tile == '6':
                    screen.blit(wooden_floor,
                                (x * tile_size[0], y * tile_size[1]))
                elif tile == '7':
                    screen.blit(wall, (x * tile_size[0], y * tile_size[1]))

                elif tile == '9':
                    screen.blit(wall, (x * tile_size[0], y * tile_size[1]))
                elif tile == '8':
                    screen.blit(wooden_floor,
                                (x * tile_size[0], y * tile_size[1]))
                elif tile == 's':
                    screen.blit(star_floor,
                                (x * tile_size[0], y * tile_size[1]))
                elif tile == 'u':  # pumpkin
                    screen.blit(grass, (x * tile_size[0], y * tile_size[1]))
                elif tile == 'a':
                    screen.blit(star_floor,
                                (x * tile_size[0], y * tile_size[1]))
                elif tile == 'j':  # pumpkin
                    screen.blit(grass, (x * tile_size[0], y * tile_size[1]))
                    screen.blit(wooden_floor,
                                (x * tile_size[0], (y) * tile_size[1]))
                elif tile == 'z':
                    screen.blit(wooden_floor,
                                (x * tile_size[0], y * tile_size[1]))

                x += 1
            y += 1

        y = 0
        for row in game_maps[place]:
            x = 0
            for tile in row:
                if tile == "4":
                    screen.blit(grass, (x * tile_size[0], (y) * tile_size[1]))
                    screen.blit(tree_images[0],
                                (x * tile_size[0], (y - 1) * tile_size[1]))
                elif tile == 'u':  # pumpkin
                    screen.blit(crops3_images[6], ((x + 0.2) * tile_size[0],
                                                   (y + 0.2) * tile_size[1]))

                elif tile == 'e':  # leaf thing
                    screen.blit(grass, (x * tile_size[0], (y) * tile_size[1]))
                    screen.blit(crops3_images[5], ((x + 0.2) * tile_size[0],
                                                   (y + 0.2) * tile_size[1]))

                elif tile == '5':
                    screen.blit(grass, (x * tile_size[0], (y) * tile_size[1]))
                    screen.blit(farm,
                                (x * tile_size[0], (y - 1) * tile_size[1]))
                elif tile == 'c':
                    screen.blit(wooden_floor,
                                (x * tile_size[0], (y) * tile_size[1]))
                    screen.blit(blossomRug,
                                (x * tile_size[0], (y) * tile_size[1]))
                elif tile == '9':
                    screen.blit(longWall,
                                (x * tile_size[0], (y) * tile_size[1]))

                elif tile == '8':
                    screen.blit(brickFirePlace,
                                (x * tile_size[0], (y) * tile_size[1]))
                elif tile == 'b':
                    screen.blit(wooden_floor,
                                (x * tile_size[0], (y) * tile_size[1]))
                    screen.blit(bookcase,
                                (x * tile_size[0], (y) * tile_size[1]))
                elif tile == 'l':
                    screen.blit(wooden_floor,
                                ((x + 0.25) * tile_size[0], y * tile_size[1]))
                    screen.blit(lamp, (x * tile_size[0], y * tile_size[1]))
                elif tile == 'y':
                    #screen.blit(wooden_floor,(x * tile_size[0], y * tile_size[1]))
                    screen.blit(yellowCouch,
                                (x * tile_size[0], (y + 1) * tile_size[1]))
                elif tile == 'm':
                    #screen.blit(wooden_floor,(x * tile_size[0], y * tile_size[1]))
                    screen.blit(moonTable,
                                (x * tile_size[0], y * tile_size[1]))
                elif tile == 's':
                    screen.blit(sunTable, (x * tile_size[0], y * tile_size[1]))
                elif tile == 'd':
                    screen.blit(grass, (x * tile_size[0], y * tile_size[1]))
                    screen.blit(dandelion,
                                (x * tile_size[0], y * tile_size[1]))
                elif tile == 'p':  # leaf thing
                    screen.blit(grass, (x * tile_size[0], y * tile_size[1]))
                    screen.blit(crop_images[0],
                                (x * tile_size[0], y * tile_size[1]))
                elif tile == 'q':  # peppers
                    screen.blit(grass, (x * tile_size[0], y * tile_size[1]))
                    screen.blit(crop_images[4],
                                (x * tile_size[0], y * tile_size[1]))
                elif tile == 'w':  # grassy thing
                    screen.blit(grass, (x * tile_size[0], y * tile_size[1]))
                    screen.blit(crop_images[10],
                                ((x + 0.5) * tile_size[0], y * tile_size[1]))
                elif tile == 'o':
                    screen.blit(wooden_floor,
                                (x * tile_size[0], (y) * tile_size[1]))
                    screen.blit(bed, (x * tile_size[0], (y) * tile_size[1]))
                elif tile == 'i':
                    #screen.blit(wooden_floor,(x * tile_size[0], y * tile_size[1]))
                    screen.blit(greenCouch,
                                (x * tile_size[0], (y + 1) * tile_size[1]))
                elif tile == 'j':
                    screen.blit(housePlant, ((x + 0.2) * tile_size[0],
                                             (y + 0.5) * tile_size[1]))
                elif tile == 'z':
                    screen.blit(fruitRug, ((x + 0.2) * tile_size[0],
                                           (y + 0.2) * tile_size[1]))
                elif tile == 'r':
                    screen.blit(wooden_floor,
                                (x * tile_size[0], y * tile_size[1]))
                    screen.blit(brownCouch,
                                (x * tile_size[0], y * tile_size[1]))
                elif tile == 'v':
                    screen.blit(wooden_floor,
                                (x * tile_size[0], y * tile_size[1]))
                    screen.blit(chair,
                                (x * tile_size[0], (y + 0.2) * tile_size[1]))

                x += 1
            y += 1

        y = 0
        for row in game_maps[place]:
            x = 0
            for tile in row:
                if tile == 'z':
                    screen.blit(oakTable, ((x + 0.5) * tile_size[0],
                                           (y + 0.2) * tile_size[1]))
                x += 1
            y += 1

        mx, my = pygame.mouse.get_pos()
        current_time = pygame.time.get_ticks()
        if current_time - last_update >= animation_cooldown:
            frame += 1
            #print("Player Rect " + str(player1.rect.center[0]))
            #print("Mouse X " + str(mx))
            last_update = current_time
            if frame >= 6:
                frame = 0

        player1.is_facing_left(player1.rect.center[0] < mx)
        for i in range(len(slimes)):
            if place == 2 and i != 0:
                if not slimes[i].is_dead:
                    slimes[i].move(player1)
            elif not slimes[i].is_dead and i == 0:
                slimes[i].move(player1)

        portals = {}
        if place == 0:
            portals = {
                (360, 0, 100, 50): (384, 480),
                (767, 240, 1, 88): (75, 288)
            }
        elif place == 1:
            portals = {(360, 556, 100, 20): (410, 120)}
        else:
            if bigslime.is_dead:
                portals = {(0, 240, 30, 88): (700, 288)}

        place = player1.enter_doors(portals, place)

        pressed_keys = pygame.key.get_pressed()
        if place != 1:
            if pressed_keys[K_RIGHT]:
                player1.move('right')
            if pressed_keys[K_LEFT]:
                player1.move('left')
            if pressed_keys[K_UP]:
                player1.move('up')
            if pressed_keys[K_DOWN]:
                player1.move('down')
        else:
            if pressed_keys[K_RIGHT]:
                player1.move('right', furniture_hitboxes)
            if pressed_keys[K_LEFT]:
                player1.move('left', furniture_hitboxes)
            if pressed_keys[K_UP]:
                player1.move('up', furniture_hitboxes)
            if pressed_keys[K_DOWN]:
                player1.move('down', furniture_hitboxes)
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_SPACE:
                    for rect in furniture_hitboxes:
                        pygame.draw.rect(screen, (0, 0, 0), rect)
                    pygame.draw.rect(screen, (255, 0, 0), player1.rect)
                    pygame.display.update()
                    time.sleep(2.5)
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    #print("Attacking")
                    attack_sound.play(0, 1500)
                    player1.attack(slime1)
                    if place == 2:
                        for i in range(1, len(slimes)):
                            player1.attack(slimes[i])
                        player1.attack(bigslime)
                    #print("Mouse X " + str(mx))
                    #print("Mouse Y " + str(my))

            if event.type == KEYUP:
                if event.key == K_LEFT or event.key == K_RIGHT:
                    player1.move('stop')
                if event.key == K_UP or event.key == K_DOWN:
                    player1.move('stop')

        for i in range(len(slimes)):
            if place == 2 and i != 0:
                if not slimes[i].is_dead:
                    slimes[i].draw(screen, frame)
            elif not slimes[i].is_dead and i == 0:
                slimes[i].draw(screen, frame)

        player1.draw(screen, frame)
        if place == 2:
            bigslime.draw(screen, frame)
        if not bigslime.is_dead and place == 2:
            pygame.draw.rect(screen, (150, 111, 214), (12, 12, 744, 36), 0, 18)
            pygame.draw.rect(screen, (0, 0, 0), (12, 12, 744, 36), 5, 18)
            draw_text(
                "Auto-Formatting, Destroyer of Worlds, Purveyor of Galaxies, The End of All",
                SMALL_CREDITS_FONT, (255, 255, 255), screen, 28, 20, 0)

        pygame.draw.rect(screen, (255, 0, 0),
                         (650, 540, player1.get_health() / 5, 24), 0, 12)
        pygame.draw.rect(screen, (0, 0, 0), (650, 540, 100, 24), 5, 12)
        screen.blit(pygame.image.load("mystic_woods/characters/health.webp"),
                    (640, 536))
        if player1.dead:
            screen.fill((178, 34, 34))
            draw_text("You Died", DEATH_FONT, (255, 255, 255), screen, 156.5,
                      235.5, 0)
            pygame.display.update()
            time.sleep(15)
            pygame.quit()
            quit()
        pygame.display.update()
        clock.tick(FPS)
