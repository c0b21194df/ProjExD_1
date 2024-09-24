import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img,True,False)
    bg_img3 = pg.transform.flip(bg_img2,True,False)
    kk_img = pg.transform.flip(pg.image.load("fig/3.png"),True,False)
    tmr = 0
    img_rct = kk_img.get_rect()
    img_rct.center = 300,200
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = tmr%3200
        
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img2,[-x+1600,0])
        screen.blit(bg_img3,[-x+3200,0])

        
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_w]:
            img_rct.move_ip((0,-1))
        if key_lst[pg.K_a]:
            img_rct.move_ip((-1,0))
        if key_lst[pg.K_d]:
            img_rct.move_ip((1,0))
        if key_lst[pg.K_s]:
            img_rct.move_ip((0,1))
        screen.blit(kk_img,img_rct)
            
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()