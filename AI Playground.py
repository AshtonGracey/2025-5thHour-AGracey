import pygame
import random
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Battle Royale with Mouse Shooting")

clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# Enemy Colors by type
ENEMY_COLORS = {
    "weak": (150, 150, 150),  # gray
    "normal": (255, 0, 0),  # red
    "strong": (139, 0, 0)  # dark red
}

# Player setup
player_size = 40
player_pos = [WIDTH // 2, HEIGHT // 2]
player_speed = 6
player_health = 100

# Bullet setup
bullet_speed = 10
bullet_size = 5
bullets = []

font = pygame.font.SysFont("Arial", 24)


class Enemy:
    def __init__(self, x, y, enemy_type="normal"):
        self.x = x
        self.y = y
        self.size = 30
        self.type = enemy_type
        self.speed = {"weak": 3, "normal": 2, "strong": 1}[enemy_type]
        self.max_health = {"weak": 10, "normal": 30, "strong": 60}[enemy_type]
        self.health = self.max_health
        self.color = ENEMY_COLORS[enemy_type]

    def move_towards(self, target_pos):
        if self.x < target_pos[0]:
            self.x += self.speed
        elif self.x > target_pos[0]:
            self.x -= self.speed
        if self.y < target_pos[1]:
            self.y += self.speed
        elif self.y > target_pos[1]:
            self.y -= self.speed

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.size, self.size))
        # Draw health bar above enemy
        health_bar_width = self.size
        health_ratio = self.health / self.max_health
        pygame.draw.rect(surface, (255, 0, 0), (self.x, self.y - 10, health_bar_width, 5))
        pygame.draw.rect(surface, (0, 255, 0), (self.x, self.y - 10, health_bar_width * health_ratio, 5))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)


def create_enemy():
    x = random.randint(0, WIDTH - 30)
    y = random.randint(0, HEIGHT - 30)
    enemy_type = random.choices(["weak", "normal", "strong"], weights=[0.4, 0.4, 0.2])[0]
    return Enemy(x, y, enemy_type)


enemy_list = [create_enemy() for _ in range(15)]  # Start with 15 enemies

# Periodically spawn more enemies
spawn_timer = 0
spawn_rate = 100  # Every 100 ticks (3-4 seconds) spawn a new enemy


def draw_health_bar(health, x, y):
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 100, 10))
    pygame.draw.rect(screen, (0, 255, 0), (x, y, health, 10))


def check_collision(rect1, rect2):
    return rect1.colliderect(rect2)


def create_bullet(x, y, direction):
    dx, dy = direction
    return [x, y, dx, dy]


running = True
while running:
    clock.tick(30)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Calculate direction from player to mouse (normalized vector)
    direction_x = mouse_x - player_pos[0]
    direction_y = mouse_y - player_pos[1]
    distance = math.sqrt(direction_x ** 2 + direction_y ** 2)

    if distance > 0:
        direction_x /= distance
        direction_y /= distance

    # Shoot when mouse button is pressed
    if pygame.mouse.get_pressed()[0]:  # Left-click
        bullet_x = player_pos[0] + player_size // 2 - bullet_size // 2
        bullet_y = player_pos[1] + player_size // 2 - bullet_size // 2
        bullets.append(create_bullet(bullet_x, bullet_y, [direction_x, direction_y]))

    # Move player with arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT]:
        player_pos[0] += player_speed
    if keys[pygame.K_UP]:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN]:
        player_pos[1] += player_speed

    # Keep player inside screen
    player_pos[0] = max(0, min(WIDTH - player_size, player_pos[0]))
    player_pos[1] = max(0, min(HEIGHT - player_size, player_pos[1]))

    # Move bullets
    for bullet in bullets[:]:
        bullet[0] += bullet[2] * bullet_speed
        bullet[1] += bullet[3] * bullet_speed
        if not (0 <= bullet[0] <= WIDTH and 0 <= bullet[1] <= HEIGHT):
            bullets.remove(bullet)

    # Move enemies towards player
    for enemy in enemy_list:
        enemy.move_towards(player_pos)

    player_rect = pygame.Rect(player_pos[0], player_pos[1], player_size, player_size)

    # Check bullet-enemy collisions
    for bullet in bullets[:]:
        bullet_rect = pygame.Rect(bullet[0], bullet[1], bullet_size, bullet_size)
        for enemy in enemy_list[:]:
            if check_collision(bullet_rect, enemy.get_rect()):
                enemy.health -= 10
                if bullet in bullets:
                    bullets.remove(bullet)
                if enemy.health <= 0:
                    enemy_list.remove(enemy)
                break

    # Check enemy-player collisions
    for enemy in enemy_list:
        if check_collision(player_rect, enemy.get_rect()):
            player_health -= 1
            if player_health <= 0:
                running = False

    # Draw player
    pygame.draw.rect(screen, GREEN, player_rect)

    # Draw enemies
    for enemy in enemy_list:
        enemy.draw(screen)

    # Draw bullets
    for bullet in bullets:
        pygame.draw.rect(screen, YELLOW, pygame.Rect(bullet[0], bullet[1], bullet_size, bullet_size))

    draw_health_bar(player_health, 20, 20)
    health_text = font.render(f"Health: {player_health}", True, BLACK)
    screen.blit(health_text, (20, 40))

    pygame.display.flip()

pygame.quit()