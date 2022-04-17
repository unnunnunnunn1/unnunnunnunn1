from pygame import*
from random import randint
img_hero='rocket.png'
img_back='galaxy.jpg'
img_asteroid='asteroid.png'
img_pulya='bullet.png'
img_tarelka='ufo.png'
class GameSprite(sprite.Sprite):
    def __init__(self, player_image,player_x,player_y,size_x,size_y,player_speed):
        sprite.Sprite.__init__(self)
        self.image=transform.scale(image.load(player_image),(size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x>3:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.y<620:
            self.rect.x += self.speed
class Enemy(GameSprite):
    def update(self):
        self.rect.y - self.speed
        if self.rect.y > win_h:
            self.rect.y = randint(80, win_h-80)
            self.rect.x = 0
font.init()
font1 = font.Font(None, 40)
clock = time.Clock()
mixer.init()   
mixer.music.load('space.ogg')
mixer.music.play()
clock=time.Clock()
width=100
height=50
color1=120
color2=100
color3=40
FPS=60
win_w=700
win_h=500
window=display.set_mode((win_w,win_h))
display.set_caption('Strelyalka')
bk=transform.scale(image.load(img_back),(win_w,win_h))
ship = Player(img_hero,5,400,80,100,2)
vrag = Enemy(img_tarelka,5,400,100,100,randint(1,7))
monsters =sprite.Group()
monsters.add(vrag)
game=True
while game:
    for e in event.get():
        if e.type ==QUIT:
            game=False
        monsters.draw(window)
        window.blit(bk,(0,0))
        ship.reset()
        ship.update()
        display.update()
        monsters.update()
clock.tick(FPS)
display.update()