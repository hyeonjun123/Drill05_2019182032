from pico2d import *
import random
import math

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

def random_hand():
    global x, y
    x = random.randint(0, TUK_WIDTH)
    y = random.randint(0, TUK_HEIGHT)

x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2  # 가야할 위치
character_x, character_y = TUK_WIDTH // 2, TUK_HEIGHT // 2  # 캐릭터의 현재 위치
random_hand()

frame = 0
hide_cursor()

while True:  # 랜덤하게 손 위치 정하기
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    hand_arrow.clip_draw(0, 0, 50, 50, x, y)  # 가야할 위치 정하고

    dx = x - character_x
    dy = y - character_y
    distance = math.sqrt(dx ** 2 + dy ** 2)

    if distance > 0:
        speed = 0.5
        character_x += (dx / distance) * speed
        character_y += (dy / distance) * speed

    character.clip_draw(frame * 100, 100 * 1, 100, 100, character_x, character_y)
    update_canvas()
    frame = (frame + 1) % 8

    if distance <= speed:
        random_hand()

close_canvas()
