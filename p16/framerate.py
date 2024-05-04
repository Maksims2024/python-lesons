import pygame
import time

SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600
FPS: int = 60


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


class Game:
    def __init__(self):
        self.rect1 = pygame.Rect(0, 200, 100, 100)
        self.rect1_speed = 100
        self.rect1_x = self.rect1.x
        self.last_time = time.time()

    def run(self):
        while True:
            # 1 визначаємо інтервал часу
            dt = time.time() - self.last_time
            self.last_time = time.time()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break

            screen.fill("White")
            pygame.draw.rect(screen, 'Red', self.rect1)

            # 2
            self.rect1_x += self.rect1_speed * dt
            self.rect1.x = self.rect1_x

            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()
