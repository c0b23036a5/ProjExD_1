import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    
    bg_img = pg.image.load("fig/pg_bg.jpg")
    Rbg_img = pg.transform.flip(bg_img,True,False)
    Kktn = pg.image.load("fig/3.png")
    Kktn = pg.transform.flip(Kktn,True,False)
    tmr = 0
    x=0
    scr_x=0
    Kktn_rct= Kktn.get_rect()
    Kktn_rct.center=300,200
    while True:
        
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst=pg.key.get_pressed()
        if key_lst[pg.K_DOWN]:
            Kktn_rct.move_ip((0,+1))
        if key_lst[pg.K_LEFT]:
            Kktn_rct.move_ip((-1,0))
        if key_lst[pg.K_RIGHT]:
            Kktn_rct.move_ip((+1,0))
        if key_lst[pg.K_UP]:
            Kktn_rct.move_ip((0,-1))
        if scr_x<=-3200:
            scr_x=0
            x=0
        scr_x=-x
        

        screen.blit(bg_img, [scr_x, 0])
        screen.blit(Rbg_img,[scr_x+1600,0])
        screen.blit(bg_img, [scr_x+3200, 0])
        screen.blit(Rbg_img,[scr_x+4800,0])
        
        screen.blit(Kktn,Kktn_rct)
        

        pg.display.update()
        tmr += 1 
        x +=1       
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()