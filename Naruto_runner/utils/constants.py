import pygame
import os

# Global Constants
TITLE = "Naruto Game Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
SOUND_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "wallpapper_naruto.png"))

ICON2 = pygame.image.load(os.path.join(IMG_DIR, "Other/reset_icon.png"))

RUN = pygame.image.load(os.path.join(IMG_DIR, "Dino/narutoRun.png"))

RUNNING = []
for i in range(4):
    img = RUN.subsurface((i*50,0), (50,60))
    img = pygame.transform.scale(img, (50*1.5, 60*1.5))
    RUNNING.append(img)


RUN_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/narutoRunShield.png"))

RUNNING_SHIELD = []
for i in range(4):
    img = RUN_SHIELD.subsurface((i*50,0), (50,60))
    img = pygame.transform.scale(img, (50*1.5, 60*1.5))
    RUNNING_SHIELD.append(img)


JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/narutoJump.png"))
JUMPING = pygame.transform.scale(JUMPING, (60*1.5, 60*1.5))

JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/narutoJumpShield.png"))
JUMPING_SHIELD = pygame.transform.scale(JUMPING_SHIELD, (60*1.5, 60*1.5))

DUCK = pygame.image.load(os.path.join(IMG_DIR, "Dino/narutoDuck.png"))

DUCKING = []
for i in range(7):
    img = DUCK.subsurface((i*50,0), (50,50))
    img = pygame.transform.scale(img, (50*1.5, 50*1.5))
    DUCKING.append(img)


DUCK_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/narutoDuckShield.png"))

DUCKING_SHIELD = []
for i in range(7):
    img = DUCK_SHIELD.subsurface((i*50,0), (50,50))
    img = pygame.transform.scale(img, (50*1.5, 50*1.5))
    DUCKING_SHIELD.append(img)


Cactus1 = pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png"))
Cactus1 = pygame.transform.scale(Cactus1, (35 * 2, 70 * 1.25))
Cactus2 = pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png"))
Cactus2 = pygame.transform.scale(Cactus2, (70 * 2, 70 * 1.25))
Cactus3 = pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png"))
Cactus3 = pygame.transform.scale(Cactus3, (105 * 1.5, 70 * 1.2))

SMALL_CACTUS = [
    Cactus1,
    Cactus2,
    Cactus3,
]

Tronco1 = pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeTronco1.png"))
Tronco1 = pygame.transform.scale(Tronco1, (45 * 2, 60 * 2))
Tronco2 = pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeTronco2.png"))
Tronco2 = pygame.transform.scale(Tronco2, (45 * 2, 60 * 2))
Tronco3 = pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeTronco3.png"))
Tronco3 = pygame.transform.scale(Tronco3, (65 * 2, 70 * 1.5))

LARGE_CACTUS = [
    Tronco1,
    Tronco2,
    Tronco3,
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/corvo1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/corvo2.png")),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/nuvem.png'))
CLOUD = pygame.transform.scale(CLOUD, (70 * 1.5, 70 * 1.5))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
SHIELD = pygame.transform.scale(SHIELD, (70 / 1.5, 70 / 1.5))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/chao.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
