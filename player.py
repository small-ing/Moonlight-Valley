import pygame
from settings import *
import spritesheet

player_sprite_sheet = pygame.image.load('mystic_woods/characters/player.png')
player_sheet = spritesheet.SpriteSheet(player_sprite_sheet)


# Creating a player class, built off the PyGame base sprite class
class Player(pygame.sprite.Sprite):
    action = 0  # 0 = idle right, 1 = walk right, 2 = walk left, 3 = idle left
    # 4 = move down, 5 = move right, 6 = move left, 7 = move down, 8 = attack right, 9 = attack left
    has_attacked_frame = [False, False, False, False]
    last_frame = None
    idle_frames = []

    for i in range(12):
        if i < 6:
            idle_frames.append(
                player_sheet.get_image(0, i, 48, 48, 2, (0, 0, 0)))
        else:
            idle_frames.append(
                pygame.transform.flip(
                    player_sheet.get_image(0, i - 6, 48, 48, 2,
                                           (0, 0, 0)).convert_alpha(), True,
                    False))

    movement_frames = []
    for i in range(12):
        if i < 6:
            movement_frames.append(
                player_sheet.get_image(1, i, 48, 48, 2, (0, 0, 0)))
        else:
            movement_frames.append(
                pygame.transform.flip(
                    player_sheet.get_image(1, i - 6, 48, 48, 2,
                                           (0, 0, 0)).convert_alpha(), True,
                    False))
    attack_frames = []
    for i in range(8):
        if i < 4:
            attack_frames.append(
                player_sheet.get_image(2, i, 48, 48, 2, (0, 0, 0)))
        else:
            attack_frames.append(
                pygame.transform.flip(
                    player_sheet.get_image(2, i - 4, 48, 48, 2,
                                           (0, 0, 0)).convert_alpha(), True,
                    False))

    def __init__(self):
        super().__init__()
        self.image = self.idle_frames[0]
        self.rect = self.image.get_rect()
        self.facing_left = False
        self.health = 500
        self.dead = False

        self.rect.center = (100, 288)

    def attack(self, slime):  # enemy, direction, frame?
        self.has_attacked_frame = [False, False, False, False]
        if self.facing_left:
            self.action = 9
            if slime.rect.collidepoint((self.rect.center[0] - 32),
                                       self.rect.center[1]):
                slime.die()
        else:
            self.action = 8
            if slime.rect.collidepoint((self.rect.center[0] + 32),
                                       self.rect.center[1]):
                slime.die()

    def move(self, direction, furniture_collisions=[]):
        is_colliding_right = False
        is_colliding_left = False
        is_colliding_up = False
        is_colliding_down = False
        if not furniture_collisions:
            if direction == 'right':
                if self.rect.x + self.rect.width <= SCREEN_WIDTH:
                    if self.facing_left:
                        self.action = 2
                    else:
                        self.action = 1
                    self.rect.move_ip(5, 0)
            elif direction == 'left':
                if self.rect.x >= 5:
                    if self.facing_left:
                        self.action = 2
                    else:
                        self.action = 1
                    self.rect.move_ip(-5, 0)
            elif direction == 'up':
                if self.rect.y >= 5:
                    if not self.facing_left:
                        self.action = 1
                    else:
                        self.action = 2
                    self.rect.move_ip(0, -5)
            elif direction == 'down':
                if self.rect.y + self.rect.height <= SCREEN_HEIGHT:
                    if not self.facing_left:
                        self.action = 1
                    else:
                        self.action = 2
                    self.rect.move_ip(0, 5)
            else:
                if not self.facing_left:
                    self.action = 0
                else:
                    self.action = 3
        else:
            is_colliding_right = False
            is_colliding_left = False
            is_colliding_up = False
            is_colliding_down = False

            collisions = []
            for i in range(len(furniture_collisions)):
                if furniture_collisions[i].colliderect(self.rect):
                    collisions.append(i)
            if len(collisions) == 0:
                pass
            else:
                for index in collisions:
                    if furniture_collisions[index].left <= self.rect.right:
                        is_colliding_right = True
                    elif furniture_collisions[index].right >= self.rect.left:
                        is_colliding_left = True
                    elif furniture_collisions[index].bottom >= self.rect.top:
                        is_colliding_up = True
                    elif furniture_collisions[index].top <= self.rect.bottom:
                        is_colliding_down = True
            if direction == 'right' and not is_colliding_right:
                if self.rect.x + self.rect.width <= SCREEN_WIDTH:
                    if self.facing_left:
                        self.action = 2
                    else:
                        self.action = 1
                    self.rect.move_ip(5, 0)
            elif direction == 'left' and not is_colliding_left:
                if self.rect.x >= 5:
                    if self.facing_left:
                        self.action = 2
                    else:
                        self.action = 1
                    self.rect.move_ip(-5, 0)
            elif direction == 'up' and not is_colliding_up:
                if self.rect.y >= 5:
                    if not self.facing_left:
                        self.action = 1
                    else:
                        self.action = 2
                    self.rect.move_ip(0, -5)
            elif direction == 'down' and not is_colliding_down:
                if self.rect.y + self.rect.height <= SCREEN_HEIGHT:
                    if not self.facing_left:
                        self.action = 1
                    else:
                        self.action = 2
                    self.rect.move_ip(0, 5)
            else:
                if not self.facing_left:
                    self.action = 0
                else:
                    self.action = 3

    def is_facing_left(self, bool):
        if bool and self.action < 8:
            self.action = 0
            self.facing_left = False
        elif not bool and self.action < 8:
            self.action = 3
            self.facing_left = True
        elif bool:
            self.facing_left = False
        else:
            self.facing_left = True

    def draw(self, surface, frame):
        #ATTACK
        if self.action > 7:
            if sum(self.has_attacked_frame) == 4:
                #print("resetting attack frames")
                self.has_attacked_frame = [False, False, False, False]
                if self.facing_left:
                    self.action = 3
                else:
                    self.action = 0
            if self.action == 8:
                if self.last_frame == frame:
                    surface.blit(
                        self.attack_frames[sum(self.has_attacked_frame)],
                        self.rect)
                else:
                    if not self.has_attacked_frame[0]:
                        #print("attack frame 1")
                        surface.blit(self.attack_frames[0], self.rect)
                        self.has_attacked_frame[0] = True
                    elif not self.has_attacked_frame[1]:
                        #print("attack frame 2")
                        surface.blit(self.attack_frames[1], self.rect)
                        self.has_attacked_frame[1] = True
                    elif not self.has_attacked_frame[2]:
                        #print("attack frame 3")
                        surface.blit(self.attack_frames[2], self.rect)
                        self.has_attacked_frame[2] = True
                    elif not self.has_attacked_frame[3]:
                        #print("attack frame 4")
                        surface.blit(self.attack_frames[3], self.rect)
                        self.has_attacked_frame[3] = True

            elif self.action == 9:
                if self.last_frame == frame:
                    surface.blit(
                        self.attack_frames[sum(self.has_attacked_frame) + 4],
                        self.rect)
                else:
                    if not self.has_attacked_frame[0]:
                        #print("attack frame 1")
                        surface.blit(self.attack_frames[4], self.rect)
                        self.has_attacked_frame[0] = True
                    elif not self.has_attacked_frame[1]:
                        #print("attack frame 2")
                        surface.blit(self.attack_frames[5], self.rect)
                        self.has_attacked_frame[1] = True
                    elif not self.has_attacked_frame[2]:
                        #print("attack frame 3")
                        surface.blit(self.attack_frames[6], self.rect)
                        self.has_attacked_frame[2] = True
                    elif not self.has_attacked_frame[3]:
                        #print("attack frame 4")
                        surface.blit(self.attack_frames[7], self.rect)
                        self.has_attacked_frame[3] = True
            self.last_frame = frame

        #IDLE
        elif self.action == 0:
            surface.blit(self.idle_frames[frame], self.rect)
        elif self.action == 3:
            surface.blit(self.idle_frames[frame + 6], self.rect)

        #WALK
        elif self.action == 1:
            surface.blit(self.movement_frames[frame], self.rect)
        elif self.action == 2:
            surface.blit(self.movement_frames[frame + 6], self.rect)

        #DEFAULT
        else:
            self.action = 0
            surface.blit(self.idle_frames[frame], self.rect)

    def enter_doors(self, doors, place):
        idx = 0
        for door in doors.keys():
            if self.rect.colliderect(pygame.Rect(door)):
                self.rect.center = doors.get(door)
                if place == 0:
                    if idx == 0:
                        return 1
                    else:
                        return 2
                else:
                    return 0
            idx += 1
        return place

    def get_health(self):
        if self.health <= 0:
            self.dead = True
        return self.health
