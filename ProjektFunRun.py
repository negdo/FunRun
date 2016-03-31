import pygame

SIRINA_EKRANA = 800
VISINA_EKRANA = 600

class Medo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        sirina = 40
        visina = 60
        self.image = pygame.Surface((sirina,visina))
        self.image.fill((200,0,0))
        self.rect = self.image.get_rect()
        self.hitrost_y = 0

    def skok(self):
        self.hitrost_y -= 5

    def update(self):
        self.hitrost_y +=0.1
        self.rect.y += self.hitrost_y
       ## self.rect.y %= VISINA_EKRANA


class Level(pygame.sprite.Sprite):
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
    tla.add(Level(0,500,800,100))

    ljudje = pygame.sprite.Group()
    papiga = Medo()
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
    
