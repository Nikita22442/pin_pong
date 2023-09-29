from pygame import *



class GameSprite():
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


    def reset(self): 
        window.blit(self.image, (self.rect.x, self.rect.y))




class Player1(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.x += self.speed
        if keys_pressed[K_s] and self.rect.y < 500 :
            self.rect.x -= self.speed  




class Player2(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_w] and self.rect.y > 0 :
            self.rect.x += self.speed
        if keys_pressed[K_s] and self.rect.y < 500 :
            self.rect.x -= self.speed




window_size = [700, 500]
window = display.set_mode(window_size)
display.set_caption("Ping pong")

clock = time.Clock()
FPS = 60





running = True

while running:
    for event in pygame.event.get():
        if event.tipe == pygame.QUIT:
            runnig = False
    display.update()
    clock.tick(FPS)
