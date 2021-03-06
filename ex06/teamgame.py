from re import S
import sys              # sysモジュールを読み込む
import pygame as pg     # pygameモジュールをpgとして読み込む
from random import randint     # randomモジュール内にあるrandint関数を読み込む
import time

bar_num = 5  # 落ちてくる障害物の最大数


# Screen クラスを定義
class Screen:
    def __init__(self, title, wh, image):   # wh:幅高さタプル, image:背景画像ファイル名
        pg.display.set_caption(title)       # タイトルバーにtitleを表示
        self.sfc = pg.display.set_mode(wh)      # Surface
        self.rct = self.sfc.get_rect()          # Rect
        self.bgi_sfc = pg.image.load(image)     # Surface
        self.bgi_rct = self.bgi_sfc.get_rect()  # Rect  

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct) 


# Player クラスを定義
class Player:
    def __init__(self, image, size, xy):    # image:画像ファイル名, size:拡大率, xy:初期座標タプル
        self.sfc = pg.image.load(image)                        # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)    # Surface
        self.rct = self.sfc.get_rect()                         # Rect
        self.rct.center = xy    # こうかとんを表示する座標をxyに設定
    
    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)
    
    def update(self, scr: Screen):
        key_states = pg.key.get_pressed() # 辞書
        if key_states[pg.K_LEFT]:
            self.rct.centerx -= 1.0
        if key_states[pg.K_RIGHT]:
            self.rct.centerx += 1.0
        if check_bound(self.rct, scr.rct) != (1, 1): # 領域外だったら
            if key_states[pg.K_LEFT]:
                self.rct.centerx += 1.0
            if key_states[pg.K_RIGHT]:
                self.rct.centerx -= 1.0
        self.blit(scr)

    # 移動するキャラクターがビームを打つメソッド
    def atack(self, scr: Screen):
        key_states = pg.key.get_pressed()
        
        if key_states[pg.K_SPACE]:
            pass


class Bar:
    def __init__(self, size, color, scr: Screen):
        self.sfc = pg.Surface(size)
        pg.Surface.fill(self.sfc, color)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = randint(0, scr.rct.width-self.rct.width)
        self.rct.centery = -randint(0, 500)
        self.w, self.h = size
        self.rct.width = randint(80, self.w)
        self.vy  = 1
    
    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)
        
    def update(self, scr: Screen):
        self.rct.move_ip(0, self.vy)
        if self.rct.centery > scr.rct.height:
            self.rct.centerx = randint(0, scr.rct.width-self.rct.width)
            self.rct.centery = -randint(0, 500)
            self.rct.width = randint(80, self.w)
        scr.sfc.blit(self.sfc, self.rct)


def check_bound(rct, scr_rct):
    
    # [1] rct: こうかとん or 爆弾のRect
    # [2] scr_rct: スクリーンのRect

    yoko, tate = 1, 1 # 領域内
    if rct.left < scr_rct.left or scr_rct.right  < rct.right:
        yoko = -1 # 領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom:
        tate = -1 # 領域外
    return yoko, tate


def main():
    sound()
    
    clock = pg.time.Clock()  # 時間計測用のオブジェクト
    screen = Screen("", (700, 900), "fig/pg_bg.jpg")
    screen.blit()

    player = Player("fig/5.png", 1.5, (350, 848))

    bars = [0 for i in range(bar_num)]
    for i in range(bar_num):
        bars[i] = Bar((120, 30), (0,0,0), screen)
        bars[i].blit(screen)
    # bar = Bar((30, 30), (125, 125, 125), screen)
    # bar.blit(screen)

    while True:
        screen.blit()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        
        player.update(screen)
        for bar in bars:
            bar.update(screen)
        
            if player.rct.colliderect(bar.rct):
                return
        
        pg.display.update()   # 画面を更新する
        clock.tick(1000)
    
    #pg.mixer.music.stop()               # 再生の終了

def sound():
    pg.mixer.init(frequency = 44100)    # 初期設定
    pg.mixer.music.load("fig/test.mp3")     # 音楽ファイルの読み込み
    pg.mixer.music.play(1)              # 音楽の再生回数(1回)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()