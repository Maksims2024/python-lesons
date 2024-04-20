import random
class Ball:
    color: tuple = (0, 0, 0)
    radius: int = 0
    weight: float = 0
    speed: int = 0
    x: int = 0
    y: int = 0

    def __init__(self, radius, weight):
        if radius > 0:
            self.radius = radius
        else:
            print('error')

        self.weight = weight

        print('start')

    def movement(self):
        self.mov_x()
        self.mov_y()

    def mov_x(self, speed_x: int = 0):
        if speed_x == 0:
            self.x += self.speed
        else:
            self.x += speed_x
    def mov_y(self, speed_x: int = 0):
        self.y += self.speed


ball_1 = Ball(12, 20)
ball_1.speed = 5

ball_1.mov_x()
print(ball_1.x, ball_1.y)
