from pico2d import load_image, load_font, draw_rectangle, get_canvas_width, get_canvas_height, clamp

import random
import common
import game_world
import game_framework

class Ball:
    def __init__(self):
        self.x = random.randint(50, common.court.w - 50)
        self.y = random.randint(50, common.court.h - 50)
        self.image = load_image('ball21x21.png')

    def draw(self):
        sx = self.x - common.court.window_left  # 화면상의 x 위치
        sy = self.y - common.court.window_bottom

        self.image.draw(sx, sy)

    def update(self):
        pass

    def get_bb(self):
        return self.x - self.image.w // 2, self.y - self.image.h // 2, self.x + self.image.w // 2, self.y + self.image.h // 2

    def handle_collision(self, group, other):
        pass