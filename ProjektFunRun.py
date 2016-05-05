import pygame

SIRINA_EKRANA = 800
VISINA_EKRANA = 600

HITROST = 4
class Medo(pygame.sprite.Sprite):
    def __init__(self, ovire = None):
        
        super().__init__()
        self.ovire = ovire
        sirina = 72
        visina = 109
        self.image = pygame.Surface((sirina,visina), pygame.SRCALPHA)
        #self.image.fill((200,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.images = pygame.image.load("papiga2.png")
       
        
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


    def update(self):

        if self.ovire:
            trki = pygame.sprite.spritecollide(self, self.ovire, False)

            for ovira in trki:
                diff = self.rect.right - ovira.rect.left
                for ov in self.ovire:
                    ov.rect.x += diff
            
        self.hitrost_y +=0.4
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

    def update(self):
        self.rect.x -= HITROST

        

        

def main():
    global skoki
    ekran = pygame.display.set_mode([SIRINA_EKRANA, VISINA_EKRANA])
    premik = 1
    
    tla = pygame.sprite.Group()
    tla.add(level(0,500,8000,100), level(500, 400, 200, 100), level(900, 400, 200, 100), level(1200, 300, 200, 50), level(1500, 300, 200, 50))
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
        tla.update()
        #Risanje
        ekran.fill((100,180,230))
        tla.draw(ekran)
        ljudje.draw(ekran)
        pygame.display.flip()
        
        

main()
    
