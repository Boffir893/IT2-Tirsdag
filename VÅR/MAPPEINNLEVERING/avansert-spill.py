import pygame  # Importerer pygame biblioteket for spillutvikling
import random  # Importerer random biblioteket for å generere tilfeldige tall

# Definisjoner av farger
WHITE = (255, 255, 255)  # Definerer fargen hvit
BLACK = (0, 0, 0)  # Definerer fargen svart
RED = (255, 0, 0)  # Definerer fargen rød

# Poengtelling
score = 0  # Setter opp en variabel for poengtelling

# Spillerklasse
class Player(pygame.sprite.Sprite):  # Definerer klassen for spilleren
    def __init__(self):  # Konstruktørmetode for spilleren
        super().__init__()  # Initialiserer overklasse (pygame.Sprite)
        self.image = pygame.Surface((50, 50))  # Oppretter en overflate for spillerens bilde
        self.image.fill(RED)  # Fyller spillerens overflate med rød farge
        self.rect = self.image.get_rect()  # Henter rektangulær område for spillerens bilde
        self.rect.center = (200, 200)  # Plasserer spilleren i midten av skjermen
        self.speed = 5  # Setter hastigheten til spilleren

    def update(self):  # Metode for å oppdatere spillerens posisjon
        keys = pygame.key.get_pressed()  # Henter tastetrykk
        if keys[pygame.K_LEFT]:  # Hvis venstre pil er trykket
            self.rect.x -= self.speed  # Flytt spilleren til venstre
        if keys[pygame.K_RIGHT]:  # Hvis høyre pil er trykket
            self.rect.x += self.speed  # Flytt spilleren til høyre
        if keys[pygame.K_UP]:  # Hvis opp-pil er trykket
            self.rect.y -= self.speed  # Flytt spilleren oppover
        if keys[pygame.K_DOWN]:  # Hvis ned-pil er trykket
            self.rect.y += self.speed  # Flytt spilleren nedover

# Hindringsklasse
class Obstacle(pygame.sprite.Sprite):  # Definerer klassen for hindringene
    def __init__(self):  # Konstruktørmetode for hindringene
        super().__init__()  # Initialiserer overklasse (pygame.Sprite)
        self.image = pygame.Surface((random.randint(20, 50), random.randint(20, 50)))  # Oppretter en tilfeldig storhet for hindringens overflate
        self.image.fill(BLACK)  # Fyller hindringens overflate med svart farge
        self.rect = self.image.get_rect()  # Henter rektangulær område for hindringens bilde
        self.rect.x = random.randrange(0, 800)  # Plasserer hindringen til en tilfeldig x-posisjon
        self.rect.y = random.randrange(-100, -40)  # Plasserer hindringen til en tilfeldig y-posisjon over skjermen
        self.speedy = random.randrange(1, 8)  # Setter tilfeldig fallhastighet for hindringen

    def update(self):  # Metode for å oppdatere hindringens posisjon
        global score  # Gjør score global slik at vi kan endre den inne i denne metoden
        self.rect.y += self.speedy  # Flytt hindringen nedover
        if self.rect.top > 600 + 10 or self.rect.left < -25 or self.rect.right > 800 + 20:  # Hvis hindringen går utenfor skjermen
            self.rect.x = random.randrange(0, 800)  # Plasserer hindringen til en tilfeldig x-posisjon
            self.rect.y = random.randrange(-100, -40)  # Plasserer hindringen til en tilfeldig y-posisjon over skjermen
            self.speedy = random.randrange(1, 8)  # Setter tilfeldig fallhastighet for hindringen
            score += 1  # Øker poengtellingen med 1

# Pygame initialisering
pygame.init()  # Initialiserer pygame biblioteket
screen_width = 800  # Setter bredden til skjermen
screen_height = 600  # Setter høyden til skjermen
screen = pygame.display.set_mode((screen_width, screen_height))  # Oppretter skjermen
pygame.display.set_caption("Platformer")  # Setter tittelen på vinduet
clock = pygame.time.Clock()  # Oppretter et klokkeobjekt for å kontrollere bildefrekvensen

# Gruppe for hindringer og spilleren
all_sprites = pygame.sprite.Group()  # Oppretter en gruppe for alle sprites
obstacles = pygame.sprite.Group()  # Oppretter en gruppe for hindringer
player = Player()  # Oppretter en spiller
all_sprites.add(player)  # Legger spilleren til gruppen for alle sprites

for _ in range(8):  # Oppretter 8 hindringer
    obstacle = Obstacle()  # Oppretter en hindring
    all_sprites.add(obstacle)  # Legger hindringen til gruppen for alle sprites
    obstacles.add(obstacle)  # Legger hindringen til hindringsgruppen

# Font for tekst
font = pygame.font.Font(None, 36)  # Oppretter en font for tekst med størrelse 36

# Hovedspill-løkke
running = True  # Setter variabelen som styrer hovedspill-løkken til sann
while running:  # Hovedspill-løkke
    for event in pygame.event.get():  # Løkke for å håndtere hendelser
        if event.type == pygame.QUIT:  # Hvis brukeren lukker vinduet
            running = False  # Avslutt hovedspill-løkken

    # Oppdater spilltilstand
    all_sprites.update()  # Oppdaterer alle sprites

    # Sjekk for kollisjoner mellom spiller og hindringer
    hits = pygame.sprite.spritecollide(player, obstacles, False)  # Sjekker for kollisjoner mellom spiller og hindringer
    if hits:  # Hvis det er en kollisjon
        running = False  # Avslutt hovedspill-løkken

    # Tegn bakgrunn
    screen.fill(WHITE)  # Fyller skjermen med hvit farge

    # Tegn alle sprites
    all_sprites.draw(screen)  # Tegner alle sprites på skjermen

    # Tegn score
    score_text = font.render("Score: " + str(score), True, BLACK)  # Oppretter tekst for poengtelling
    screen.blit(score_text, (10, 10))  # Tegner poengtelling på skjermen

    # Oppdater skjermen
    pygame.display.flip()  # Oppdaterer skjermen med alle endringer

    # Hold konstant bildefrekvens
    clock.tick(60)  # Begrenser bildefrekvensen til 60 bilder per sekund

pygame.quit()  # Avslutter pygame og lukker vinduet

