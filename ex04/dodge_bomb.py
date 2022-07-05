from re import L
import pygame as pg
import sys

def main():

    clock = pg.time.Clock()
    pg.display.set_caption("逃げろ！こうかとん")
    screen_sfc = pg.display.set_mode((1600, 900))   #surface
    screen_rect = screen_sfc.get_rect()             #Rect
    bgimg_sfc =pg.image.load("fig/pg_bg.jpg")       #surface
    bgimg_rect = bgimg_sfc.get_rect()               #Rect
    screen_sfc.blit(bgimg_sfc, bgimg_rect)
    #pg.display.update()　#試し
    kkimg_sfc = pg.image.load("fig/6.png")          #Surface
    kkimg_sfc =pg.transform.rotozoom(kkimg_sfc, 0, 2.0) #Surface
    kkimg_rect = kkimg_sfc.get_rect()               #Rect
    kkimg_rect.center = 900, 400

    while True:
        screen_sfc.blit(bgimg_sfc, bgimg_rect)
        screen_sfc.blit(kkimg_sfc, kkimg_rect)
        #練習2
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return #xが押されたらmain関数return
        pg.display.update()
        clock.tick(1000)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit