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
    L_=1
    R_=1
    U_=1
    D_=1
    l_=0
    r_=0
    u_=0
    d_=0
    l_p=0
    r_p=0
    u_p=0
    d_p=0
    while True:
        
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst=pg.key.get_pressed()
        

        if key_lst[pg.K_DOWN] and (d_==0 or d_p<d_):
            Kktn_rct.move_ip((0,+1))
            d_p=d_
            D_=0
            d_+=1
        else:
            D_=1
            d_=d_p
        if key_lst[pg.K_LEFT] and (l_==0 or l_p<l_):
            Kktn_rct.move_ip((-1,0))
            L_=0
            l_p=l_
            l_+=1
        else:
            L_=1
            l_=l_p
        if key_lst[pg.K_RIGHT] and (r_==0 or r_p<r_):
            Kktn_rct.move_ip((+2,0))
            R_=0
            r_p=r_
            r_+=1
        else:
            R_=1
            r_=r_p
        if key_lst[pg.K_UP] and (u_==0 or u_p<u_):
            Kktn_rct.move_ip((0,-1))
            U_=0
            u_p=u_
            u_+=1
        else:
            U_=1
            u_=u_p
        if L_+R_+U_+D_==4:
            Kktn_rct.move_ip((-1,0))
            
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