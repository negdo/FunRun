import pygame

SIRINA_EKRANA = 800
VISINA_EKRANA = 600

class Medo(pygame.sprite.Sprite):
    def __init__(self, ovire = None):
        super().__init__()
        self.ovire = ovire
        sirina = 87
        visina = 123
        self.image = pygame.Surface((sirina,visina), pygame.SRCALPHA)
        #self.image.fill((200,0,0))
        self.rect = self.image.get_rect()
        self.images = pygame.image.load("papiga1.png")

        
        self.hitrost_y = 0
        self.nastavi_sliko()

        
    def nastavi_sliko(self):
        self.image.fill((0, 0, 0, 0))
        self.image.blit(self.images, (0, 0),(0, 0, 87, 123))

            
    def skok(self):
        self.hitrost_y -= 10

        trki = pygame.sprite.spritecollide(self, self.ovire, False)
        if len(trki):
            self.hitrost_y = -10


    def update(self):
        
        self.hitrost_y +=0.3
        self.rect.y += self.hitrost_y
       ## self.rect.y %= VISINA_EKRANA
        if self.ovire:
            trki = pygame.sprite.spritecollide(self, self.ovire, False)
            for ovira in trki:
                if self.hitrost_y < 0:
                    self.rect.top = ovira.rect.bottom
                if self.hitrost_y > 0:
                    self.rect.bottom = ovira.rect.top
                self.hitrost_y = 0


        
class level(pygame.sprite.Sprite):
    def __init__(self, x, y, s, v):
        super().__init__()
        self.image = pygame.Surface((s, v))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image.fill((50,150,50))


def main():
    ekran = pygame.display.set_mode([SIRINA_EKRANA, VISINA_EKRANA])

    tla = pygame.sprite.Group()
    tla.add(level(0,500,800,100))

    ljudje = pygame.sprite.Group()
    papiga = Medo(tla)
    ljudje.add(papiga)

    konec_zanke = False
    ura = pygame.time.Clock()
    while not konec_zanke:
        ura.tick(60)
        for dogodek in pygame.event.get():
            if dogodek.type == pygame.KEYDOWN:
                if dogodek.key == pygame.K_UP:
                    papiga.skok()

        #Fizika
        ljudje.update()
        #Risanje
        ekran.fill((0,0,200))
        tla.draw(ekran)
        ljudje.draw(ekran)
        pygame.display.flip()
        
        

main()
    
