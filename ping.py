from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 395:
            self.rect.y += self.speed
            
    def update2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y< 395:
            self.rect.y += self.speed
    
# окно
back= 124, 246, 234

window = display.set_mode((700,500))
display.set_caption('Супер Ping')
run = True
finish = False
FPS = 60
clock = time.Clock()
window.fill(back)

background = transform.scale(image.load("поле.jpg"), (700,500)) 

win_height=500

speed_x = 3
speed_y = 3

font.init()
font= font.Font(None, 35)

lose1 = font.render("Player 1 lost!", True, (180, 0, 0))
lose2 = font.render("Player 2 lost!", True, (180, 0, 0))

# персонажи
rack1 = Player('ракетка.jpg', 5, 400, 80, 100, 4)
rack2 = Player('ракетка.jpg', 615, 400, 80, 100, 4)
bal= GameSprite('мяч.jpg', 1, 25, 50, 50, 4)

# цикл                   
while run:   
    for e in event.get():   
        if e.type == QUIT:
            run = False
    
    if not finish:
        window.blit(background, (0,0))
            
        rack1.update1()
        rack2.update2()      
        # bal.update()

        rack1.reset()
        rack2.reset()
        bal.reset()
    
        
        bal.rect.x += speed_x
        bal.rect.y += speed_y
        
        if  bal.rect.y > win_height-50 or bal.rect.y < 0:
            speed_y *= -1

        if sprite.collide_rect(rack1, bal) or sprite.collide_rect(rack2, bal):
            speed_x *= -1
            speed_y *= 1

        # проигрыш
        if  bal.rect.x < 0:
            finish = True
            window.blit(lose1, (250, 350))
            # run=True

        if  bal.rect.x > 700:
            finish = True
            window.blit(lose2, (250, 350))
            # run=True
            
    display.update()     
    clock.tick(FPS)
