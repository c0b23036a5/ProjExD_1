import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    clock.tick(200)
    bg_img = pg.image.load("fig/pg_bg.jpg")
    Kktn = pg.image.load("fig/3.png")
    Kktn = pg.transform.flip(Kktn,True,False)
    tmr = 0
    slide_x=0
    scr_x=0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        
        if scr_x<=-800:
            scr_x=0
            slide_x=0
        scr_x=-slide_x*20
        

        screen.blit(bg_img, [scr_x, 0])
        screen.blit(Kktn,[300,200])
        

        pg.display.update()
        tmr += 1 
        slide_x +=1       
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()