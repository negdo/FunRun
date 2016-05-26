import pygame

SIRINA_EKRANA = 800
VISINA_EKRANA = 600

HITROST = 4
class Medo(pygame.sprite.Sprite):
    def __init__(self, ovire = None, ovire2 = None):
        
        super().__init__()
        self.ovire = ovire
        self.ovire2 = ovire2
        sirina = 72
        visina = 109
        self.image = pygame.Surface((sirina,visina), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.images = pygame.image.load("papiga2.png")

       
        self.hitrost_x = 0
        self.hitrost_y = 0
        self.nastavi_sliko()        

        
    def nastavi_sliko(self):
        self.image.fill((0, 0, 0, 0))
        self.image.blit(self.images, (0, 0),(0, 0, 87, 123))

            
    def skok(self):
        self.rect.y += 2
        trki = pygame.sprite.spritecollide(self, self.ovire, False)
        self.rect.y -= 2
        if len(trki):
            self.hitrost_y = -10


    def levo(self):
        self.hitrost_x = -3

    def desno(self):
        self.hitrost_x = 3

    def stop(self):
        self.hitrost_x = 0
  

    def update(self):

        self.rect.x += self.hitrost_x

        if self.ovire:
            trki = pygame.sprite.spritecollide(self, self.ovire, False)
            for ovira in trki:
                # diff = self.rect.right - ovira.rect.left
                self.rect.right = ovira.rect.left
                self.hitrost_x = 0
        if self.ovire2:
            trki2 = pygame.sprite.spritecollide(self, self.ovire2, False)
            for ovira in trki2:                     
                pygame.quit()
                print("Boom")
                
            
        self.hitrost_y +=0.4
        self.rect.y += self.hitrost_y
##        if self.rect.bottom > 500:
##            self.hitrost_y=0
##            self.rect.bottom = 500
       ## self.rect.y %= VISINA_EKRANA
        if self.ovire:
            trki = pygame.sprite.spritecollide(self, self.ovire, False)
            for ovira in trki:
                if self.hitrost_y < 0:
                    self.rect.top = ovira.rect.bottom
                if self.hitrost_y > 0:
                    self.rect.bottom = ovira.rect.top
                self.hitrost_y = 0


        if self.ovire2:
            trki2 = pygame.sprite.spritecollide(self, self.ovire, False)
            for ovira in trki2:
                pygame.quit()





class nevarnost(pygame.sprite.Sprite):
    def __init__(self, x, y, s, v, perioda = False, premika = True):
        super().__init__()
        self.premika = premika
        self.perioda = perioda
        self.image = pygame.Surface((s, v), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.images = pygame.image.load("znak4.png")
        self.nastavi_sliko()
        
    def nastavi_sliko(self):
        self.image.fill((0, 0, 0, 0))
        self.image.blit(self.images, (0, 0),(0, 0, 54, 85))

    def update(self):
        if self.premika:
            self.rect.x -= HITROST
            if self.perioda:
                if self.rect.x < -self.perioda:
                    self.rect.x = SIRINA_EKRANA - HITROST
        

        
class level(pygame.sprite.Sprite):
    
    def __init__(self, x, y, s, v, perioda=False, premika=True, slika=None):
        super().__init__()
        self.premika = premika
        self.perioda = perioda
        self.image = pygame.Surface((s, v))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image.fill((50,150,50))
        self.images = pygame.image.load("tla2.png")

        self.nastavi_sliko()
        
    def nastavi_sliko(self):
        self.image.fill((0, 0, 0, 0))
        self.image.blit(self.images, (0, 0),(0, 0, 1150, 110))


    def update(self):
        if self.premika:
            self.rect.x -= HITROST
            if self.perioda:
                if self.rect.x < -self.perioda:
                    self.rect.x = SIRINA_EKRANA - HITROST
                    

        

        

def main():
    global skoki
    ekran = pygame.display.set_mode([SIRINA_EKRANA, VISINA_EKRANA])
    premik = 1
    
    tla = pygame.sprite.Group()
    tla.add(
        level(0, 490, SIRINA_EKRANA, VISINA_EKRANA, SIRINA_EKRANA),
        level(SIRINA_EKRANA, 490, SIRINA_EKRANA, VISINA_EKRANA, SIRINA_EKRANA),
        level(500, 450, 200, 90, 2000),
        level(900, 450, 200, 90, 2000),
        level(1300, 300, 200, 50, 1300),
        level(1600, 300, 200, 50, 1300))
    ljudje = pygame.sprite.Group()
    nevarnosti = pygame.sprite.Group()
    nevarnosti.add(nevarnost(700, 405, 54, 85, 1000))

    papiga = Medo(tla, nevarnosti)
    ljudje.add(papiga)


    konec_zanke = False
    ura = pygame.time.Clock()
    while not konec_zanke:
        ura.tick(60)
        for dogodek in pygame.event.get():
            if dogodek.type == pygame.QUIT:
                konec_zanke = True
                
            elif dogodek.type == pygame.KEYDOWN:
                
                if dogodek.key == pygame.K_UP:
                    papiga.skok()
                elif dogodek.key == pygame.K_LEFT:
                    papiga.levo()
                elif dogodek.key == pygame.K_RIGHT:
                    papiga.desno()

            elif dogodek.type == pygame.KEYUP:
                if dogodek.key == pygame.K_LEFT:
                    papiga.stop()
                elif dogodek.key == pygame.K_RIGHT:
                    papiga.stop()

        if papiga.rect.x < 0:
            konec_zanke = True
        

        #Fizika
        ljudje.update()
        tla.update()
        nevarnosti.update()
        #Risanje
        ekran.fill((100,180,230))
        tla.draw(ekran)
        ljudje.draw(ekran)
        nevarnosti.draw(ekran)
        pygame.display.flip()
    pygame.quit()        
        
        

main()
    
