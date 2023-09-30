from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

def handle_events():
    global x, y

    x = random.randint(0,TUK_WIDTH)
    y = random.randint(0,TUK_HEIGHT)

    pass

x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2 #가야할 위치
x1,y1 = 0,0
x2,y2 = 0,0


frame = 0
hide_cursor()

while True: #랜덤하게 손 위치 정하기
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    hand_arrow.clip_draw(0, 0, 50, 50, x, y) #가야할 위치 정하고
    delay(0.5) #시간 딜레이


    character.clip_draw(frame * 100, 100 * 1, 100, 100, x2, y2)
    update_canvas()
    frame = (frame + 1) % 8


    delay(0.03)
    handle_events()


close_canvas()




