import pygame as pg
import sys
import random

class sho:
    def __init__(self, size):
        self.sfc = pg.Surface((2*size, 2*size)) #Surface
        self.sfc.set_colorkey((0, 0, 0))

class Screen:
    def __init__(self, title, wh, image):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)   #surface
        self.rct = self.sfc.get_rect()             #Rect
        self.bgi_sfc =pg.image.load(image)       #surface
        self.bgi_rct = self.bgi_sfc.get_rect()               #Rect

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)
       

class Bird:
    def __init__(self, image, size, xy):
        self.sfc = pg.image.load(image)          #Surface
        self.sfc =pg.transform.rotozoom(self.sfc, 0, size) #Surface
        self.rct = self.sfc.get_rect()               #Rect
        self.rct.center = xy
    def blit(self, scr: Screen): #型を指定する
        #screen_sfc.blit(kkimg_sfc, kkimg_rect)
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        key_states = pg.key.get_pressed() #辞書
        if key_states[pg.K_UP]:
            self.rct.centery -= 1 #key Upが押されてたらy座標-1
        if key_states[pg.K_DOWN]:
            self.rct.centery += 1
        if key_states[pg.K_LEFT]:
            self.rct.centerx -= 1
        if key_states[pg.K_RIGHT]:
            self.rct.centerx += 1
        if check_bound(self.rct, scr.rct) != (1,1):#領域外だったら
            if key_states[pg.K_UP]:
                self.rct.centery += 1 #key Upが押されてたらy座標-1
            if key_states[pg.K_DOWN]:
                self.rct.centery -= 1
            if key_states[pg.K_LEFT]:
                self.rct.centerx += 1
            if key_states[pg.K_RIGHT]:
                self.rct.centerx -= 1
        self.blit(scr)

class Bomb():
    def __init__(self, color, size, vxy, scr: Screen):
        self.sfc = pg.Surface((2*size, 2*size)) #Surface
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, color, (size, size), size)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy #練習６

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)
    def update(self, scr: Screen):
        #練習６
        self.rct.move_ip(self.vx, self.vy) 
        #練習７
        yoko, tate =check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        #練習5
        self.blit(scr)
        
def main():
    clock = pg.time.Clock()

    

    scr = Screen("逃げろ！こうかとん", (1800, 900), "fig/pg_bg.jpg")

    
    kkt = Bird("fig/6.png", 2.0, (900, 400))
    
    bkd = Bomb((255,0,0), 10, (+1,+1), scr)

    while True:
        
        scr.blit()
        
        #練習2
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return #xが押されたらmain関数return
        
        kkt.update(scr)
        
        
        bkd.update(scr)

        
        if kkt.rct.colliderect(bkd.rct): #爆弾インスタンスのrct変数
            return

        pg.display.update()
        clock.tick(1000)
#練習7
def check_bound(rct, scr_rct):
    # rct:こうかとんor 爆弾のRect
    # scr_rct:　スクリーンのRect
    yoko, tate = +1, +1 #領域内
    if rct.left < scr_rct.left or scr_rct.right < rct.right:
        yoko = -1 #領域外
    if rct.top < scr_rct.top or scr_rct.bottom < rct.bottom:
        tate = -1 #領域外
    return yoko, tate
if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit