from pygame import *


window = display.set_mode((700, 600))
display.set_caption("Ping Pong")
clock = time.Clock()


class ImageSprite(sprite.Sprite):
    def __init__(self, file, position, size, speed=(0, 0)):
        super().__init__()
        self.image = image.load(file)
        self.image = transform.scale(self.image, size)
        self.rect = Rect(position, size)
        self.speed = Vector2(speed)
    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)


class Ball(ImageSprite):
    def update(self):
        self.rect.topleft += self.speed

class Player(ImageSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_s]:
            self.rect.y += self.speed.y
        if keys[K_w]:
            self.rect.y -= self.speed.y

        if self.rect.top >= 700:
            self.rect.top = 700
        if self.rect.left <= 0:
            self.rect.left = 0

class Player2(ImageSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_DOWN]:
            self.rect.y += self.speed.y
        if keys[K_UP]:
            self.rect.y -= self.speed.y
 
        if self.rect.top >= 700:  
            self.rect.top = 700
        if self.rect.left <= 0:
            self.rect.left = 0

p1 = Player(file="paddle1.png", position=(0, 200), size=(80, 80), speed=8)
p2 = Player2(file="paddle2.png", position=(600, 200), size=(80, 80), speed=8)
ball = Ball(file="ball.png", position=(50, 50), size=(80, 80), speed=(2,3))

game_on = True
 
while game_on:
 
    for ev in event.get():
 
        if ev.type == QUIT:
            game_on = False
    window.fill((255, 255, 255))
    
    p1.update()
    p1.draw(window)
    p2.update()
    p2.draw(window)
    ball.update()
    ball.draw(window)
    display.update()
    clock.tick(60)




