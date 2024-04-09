import pygame  # Importerer pygame-biblioteket for spillgrafikk
import random  # Importerer random-modulen for tilfeldige tall

# Initialiserer pygame
pygame.init()

# Definerer vindusstørrelsen
WIDTH, HEIGHT = 800, 600  # Setter bredden og høyden til spillvinduet
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # Oppretter spillvinduet med angitt størrelse
pygame.display.set_caption("Snake Game")  # Setter tittelen på spillvinduet

# Definerer farger
WHITE = (255, 255, 255)  # Setter fargen hvit 
BLACK = (0, 0, 0)  # Setter fargen svart 
RED = (255, 0, 0)  # Setter fargen rød 

# Definerer konstanter
BLOCK_SIZE = 20  # Setter størrelsen på hvert blokk i spillet
FPS = 10  # Setter antall oppdateringer per sekund for spillet

# Definerer retninger som konstanter
UP = (0, -1)  # Definerer bevegelsesretning opp
DOWN = (0, 1)  # Definerer bevegelsesretning ned
LEFT = (-1, 0)  # Definerer bevegelsesretning venstre
RIGHT = (1, 0)  # Definerer bevegelsesretning høyre

clock = pygame.time.Clock()  # Oppretter en klokke for å styre oppdateringshastigheten

# Klasse for Snake (slange) i spillet
class Snake:
    def __init__(self):
        self.length = 1  # Lengden på slangen
        self.positions = [((WIDTH // 2), (HEIGHT // 2))]  # Startposisjonen til slangen
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])  # Startbevegelsesretning til slangen
        self.color = RED  # Fargen til slangen
        self.score = 0  # Spillerens poeng

    def get_head_position(self):  # Metode for å få hodeposisjonen til slangen
        return self.positions[0]

    def turn(self, point):  # Metode for å endre bevegelsesretning til slangen
        if self.length > 1 and (point[0]*-1, point[1]*-1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):  # Metode for å bevege slangen
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x*BLOCK_SIZE)) % WIDTH), (cur[1] + (y*BLOCK_SIZE)) % HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):  # Metode for å tilbakestille slangen
        self.length = 1
        self.positions = [((WIDTH // 2), (HEIGHT // 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.score = 0

    def draw(self, surface):  # Metode for å tegne slangen på spillvinduet
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, WHITE, r, 1)

# Klasse for mat (food) i spillet
class Food:
    def __init__(self):  # Initialiserer matobjektet
        self.position = (0, 0)  # Setter matens posisjon
        self.color = WHITE  # Fargen til maten
        self.randomize_position()  # Genererer en tilfeldig posisjon for maten

    def randomize_position(self):  # Metode for å generere en tilfeldig posisjon for maten
        self.position = (random.randint(0, (WIDTH // BLOCK_SIZE) - 1) * BLOCK_SIZE,
                         random.randint(0, (HEIGHT // BLOCK_SIZE) - 1) * BLOCK_SIZE)

    def draw(self, surface):  # Metode for å tegne maten på spillvinduet
        r = pygame.Rect((self.position[0], self.position[1]), (BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, BLACK, r, 1)

def main():  # Hovedfunksjonen for å kjøre spillet
    snake = Snake()  # Oppretter et Snake-objekt
    food = Food()  # Oppretter et Food-objekt
    running = True  # Variabel for å kontrollere løkkekjøring

    while running:  # Hovedspill-løkken
        for event in pygame.event.get():  # Håndterer hendelser i spillet
            if event.type == pygame.QUIT:  # Hvis brukeren lukker spillvinduet
                running = False  # Avslutter hovedløkken
            elif event.type == pygame.KEYDOWN:  # Hvis brukeren trykker på en tast
                if event.key == pygame.K_UP:  # Hvis brukeren trykker på pil opp-tasten
                    snake.turn(UP)  # Slangen snur seg oppover
                elif event.key == pygame.K_DOWN:  # Hvis brukeren trykker på pil ned-tasten
                    snake.turn(DOWN)  # Slangen snur seg nedover
                elif event.key == pygame.K_LEFT:  # Hvis brukeren trykker på pil venstre-tasten
                    snake.turn(LEFT)  # Slangen snur seg til venstre
                elif event.key == pygame.K_RIGHT:  # Hvis brukeren trykker på pil høyre-tasten
                    snake.turn(RIGHT)  # Slangen snur seg til høyre

        snake.move()  # Beveger slangen

        if snake.get_head_position() == food.position:  # Hvis slangen spiser maten
            snake.length += 1  # Slangen vokser
            snake.score += 1  # Spillerens poeng øker
            food.random
