import pygame
import spritesheet

slime_sprite_sheet = pygame.image.load('mystic_woods/characters/slime.png')
slime_sheet = spritesheet.SpriteSheet(slime_sprite_sheet)


class Small_Slime(pygame.sprite.Sprite):
    idle_frames = []
    has_played_death_frame = [False, False, False, False, False]
    last_frame = None
    is_dead = False
    for i in range(8):
        if i < 4:
            idle_frames.append(
                pygame.transform.flip(
                    slime_sheet.get_image(0, i, 32, 32, 1,
                                          (0, 0, 0)).convert_alpha(), True,
                    False))
        else:
            idle_frames.append(
                slime_sheet.get_image(0, i - 4, 32, 32, 1, (0, 0, 0)))
    death_frames = []
    for i in range(10):
        if i < 5:
            death_frames.append(
                pygame.transform.flip(
                    slime_sheet.get_image(4, i, 32, 32, 1,
                                          (0, 0, 0)).convert_alpha(), True,
                    False))
        else:
            death_frames.append(
                pygame.transform.flip(
                    slime_sheet.get_image(4, i - 5, 32, 32, 1,
                                          (0, 0, 0)).convert_alpha(), True,
                    False))

    def __init__(self, y=288):
        super().__init__()
        self.image = self.idle_frames[0]
        self.rect = self.image.get_rect()
        self.rect.center = (600, y)

    def move(self, player):
        x_from_player = abs(self.rect.center[0] - player.rect.center[0])
        y_from_player = abs(self.rect.center[1] - player.rect.center[1])

        if x_from_player > y_from_player:
            if self.rect.center[0] > player.rect.center[0]:
                self.rect.move_ip(-4, 0)
            else:
                self.rect.move_ip(4, 0)
        else:
            if self.rect.center[1] > player.rect.center[1]:
                self.rect.move_ip(0, -4)
            else:
                self.rect.move_ip(0, 4)
        if x_from_player < 25 and y_from_player < 25:
            player.health -= 1

    def draw(self, surface, frame):
        if frame <= 3 and not self.is_dead:
            surface.blit(self.idle_frames[frame], self.rect)
        elif frame != self.last_frame and not self.is_dead:
            frame = frame % 4
            surface.blit(self.idle_frames[frame], self.rect)

        # only possible if slime is dead
        # tests whether entire animation has played out, if so skips
        elif frame != self.last_frame:
            self.last_frame = frame
            if not self.has_played_death_frame[0]:
                surface.blit(self.death_frames[0], self.rect)
                self.has_played_death_frame[0] = True
            elif not self.has_played_death_frame[1]:
                surface.blit(self.death_frames[1], self.rect)
                self.has_played_death_frame[1] = True
            elif not self.has_played_death_frame[2]:
                surface.blit(self.death_frames[2], self.rect)
                self.has_played_death_frame[2] = True
            elif not self.has_played_death_frame[3]:
                surface.blit(self.death_frames[3], self.rect)
                self.has_played_death_frame[3] = True
            elif not self.has_played_death_frame[4]:
                surface.blit(self.death_frames[4], self.rect)
                self.has_played_death_frame[4] = True
            else:
                pass
        else:
            pass

    def die(self):
        self.is_dead = True
        self.rect.center = (-100, -100)
