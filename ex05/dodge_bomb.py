import pygame as pg
import sys
import random



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
            self.rct.centery -= 2 #key Upが押されてたらy座標-1
        if key_states[pg.K_DOWN]:
            self.rct.centery += 2
        if key_states[pg.K_LEFT]:
            self.rct.centerx -= 2
        if key_states[pg.K_RIGHT]:
            self.rct.centerx += 2
        if check_bound(self.rct, scr.rct) != (1,1):#領域外だったら
            if key_states[pg.K_UP]:
                self.rct.centery += 2 #key Upが押されてたらy座標-1
            if key_states[pg.K_DOWN]:
                self.rct.centery -= 2
            if key_states[pg.K_LEFT]:
                self.rct.centerx += 2
            if key_states[pg.K_RIGHT]:
                self.rct.centerx -= 2
        self.blit(scr)



class Bomb():
    def __init__(self, color, size, vxy, scr: Screen):
        self.sfc = pg.Surface((3*size, 3*size)) #Surface
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, color, (size, size), size)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy #練習6

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

class Bom():
    def __init__(self, color, size, vxy, scr: Screen):
        self.sfc = pg.Surface((2*size, 2*size)) #Surface
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, color, (size, size), size)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)
    def update(self, scr: Screen):
        self.rct.move_ip(self.vx, self.vy) 
        yoko, tate =check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr) #追加のボール

class h1():
    def __init__(self, size, vxy, scr: Screen):
        self.sfc = pg.Surface((size, 10*size)) #Surface
        self.sfc.set_colorkey((255, 0, 0))
        self.rct = self.sfc.get_rect()
        self.vx, self.vy = vxy 

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)
    def update(self, scr: Screen):
        self.rct.move_ip(self.vx, self.vy) 
        yoko, tate =check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        
        self.blit(scr) #上に固定されている壁を追加 

class h2():
    def __init__(self, size, vxy, scr: Screen):
        self.sfc = pg.Surface((5*size, 10*size)) #Surface
        self.sfc.set_colorkey((255, 0, 0))
        self.rct = self.sfc.get_rect()
        self.rct.centery = random.randint(0, scr.rct.height)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy 

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)
    def update(self, scr: Screen):
        self.rct.move_ip(self.vx, self.vy) 
        yoko, tate =check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        
        self.blit(scr) #ランダムに配置される壁を追加
        
def main():
    clock = pg.time.Clock()

    

    scr = Screen("逃げろ！こうかとん", (1600, 900), "fig/pg_bg.jpg")

    
    kkt = Bird("fig/6.png", 2.0, (900, 400))
    
    bkd = Bomb((255,0,0), 10, (+1,+1), scr)
    bo = Bom((0,255,0), 30, (+2,+2), scr)

    sh = h1( 30, (+1, 0), scr)
    h = h2( 30, (+2, 0), scr)

    while True:
        
        scr.blit()

        
        
        #練習2
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return #xが押されたらmain関数return
        
        kkt.update(scr)
        
        bkd.update(scr)
        bo.update(scr)

        sh.update(scr)

        h.update(scr)

        
        if kkt.rct.colliderect(bkd.rct): #爆弾インスタンスのrct変数
            return
        if kkt.rct.colliderect(bo.rct): 
            return
        if kkt.rct.colliderect(sh.rct): 
            return
        if kkt.rct.colliderect(h.rct): 
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