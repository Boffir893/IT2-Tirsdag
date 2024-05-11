import pygame, random


pygame.init()


skjerm = pygame.display.set_mode((1000, 600))
skjerm_bredde = 1000
skjerm_hoyde = 600



white = "white"
svart = "black"



font = pygame.font.Font(None, 36)


class SpillObjekt:
    def __init__(self, x, y, bredde, høyde):
        self.rektangel = pygame.Rect(x, y, bredde, høyde)

    def tegn(self, farge):
        pygame.draw.rect(skjerm, farge, self.rektangel)
    
    def plassering(self, x: int, y: int):
        self.rect.center = (x, y)



class Paddle(SpillObjekt): 
    def __init__(self, x, y):
        super().__init__(x, y, 20, 120)


class Ball(SpillObjekt): 
    def __init__(self):
        super().__init__(500, 300, 20, 20)
        self.dx = 1.9
        self.dy = -1.9

    def oppdater(self):
        self.rektangel.move_ip(self.dx, self.dy)



class Poeng:
    def __init__(self): 
        self.venstre_spiller = 0
        self.høyre_spiller = 0

    def vis(self): 
        font = pygame.font.Font(None, 56)
        tekst = font.render(f'{self.venstre_spiller} : {self.høyre_spiller}', True, white)
        skjerm.blit(tekst, (465, 20))


class PongSpill:
    def __init__(self):
        self.venstre_paddle = Paddle(10, 240)
        self.høyre_paddle = Paddle(970, 240)
        self.ball = Ball()
        self.poeng = Poeng()
        self.kjører = True
        self.pause = False  


    def håndter_hendelser(self):
        for hendelse in pygame.event.get():
            if hendelse.type == pygame.QUIT:
                self.kjører = False
            
        taster = pygame.key.get_pressed()
        if taster[pygame.K_w]:
            self.venstre_paddle.rektangel.move_ip(0, -2)
        if taster[pygame.K_s]:
            self.venstre_paddle.rektangel.move_ip(0, 2)


        if taster[pygame.K_UP]:
            self.høyre_paddle.rektangel.move_ip(0, -2)
        if taster[pygame.K_DOWN]:
            self.høyre_paddle.rektangel.move_ip(0, 2)



    def oppdater(self):
        if not self.pause:
            self.ball.oppdater()

            if self.ball.rektangel.top <= 0 or self.ball.rektangel.bottom >= 600:
                self.ball.dy *= -1

            if self.ball.rektangel.left <= 0:
                self.poeng.høyre_spiller += 1
                self.ball = Ball()
            if self.ball.rektangel.right >= 1000:
                self.poeng.venstre_spiller += 1
                self.ball = Ball()

            if self.ball.rektangel.colliderect(self.venstre_paddle.rektangel) or self.ball.rektangel.colliderect(self.høyre_paddle.rektangel):
                self.ball.dx *= -1

    def tegn(self):
        skjerm.fill(svart)
        self.venstre_paddle.tegn(white)
        self.høyre_paddle.tegn(white)
        self.ball.tegn(white)
        self.poeng.vis()

        

        pygame.display.flip()

    def kjør(self):
        while self.kjører:
            self.håndter_hendelser()
            self.oppdater()
            self.tegn()

        pygame.quit()

if __name__ == "__main__":
    spill = PongSpill()
    spill.kjør()
