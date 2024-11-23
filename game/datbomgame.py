import pygame
import sys
import time

# Khởi tạo pygame
pygame.init()

# Kích thước cửa sổ
WIDTH, HEIGHT = 600, 600
TILE_SIZE = 40
ROWS = HEIGHT // TILE_SIZE
COLS = WIDTH // TILE_SIZE

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# Khởi tạo màn hình
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bomberman")

# Tải ảnh (nếu có)
player_image = pygame.Surface((TILE_SIZE, TILE_SIZE))
player_image.fill(GREEN)

bomb_image = pygame.Surface((TILE_SIZE, TILE_SIZE))
bomb_image.fill(RED)

explosion_image = pygame.Surface((TILE_SIZE, TILE_SIZE))
explosion_image.fill(YELLOW)

# Nhân vật chính
player = {"x": 1, "y": 1}

# Danh sách các quả bom
bombs = []
explosions = []

# Hàm vẽ lưới
def draw_grid():
    for x in range(0, WIDTH, TILE_SIZE):
        pygame.draw.line(screen, WHITE, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, TILE_SIZE):
        pygame.draw.line(screen, WHITE, (0, y), (WIDTH, y))

# Hàm vẽ nhân vật
def draw_player():
    screen.blit(player_image, (player["x"] * TILE_SIZE, player["y"] * TILE_SIZE))

# Hàm vẽ bom
def draw_bombs():
    for bomb in bombs:
        screen.blit(bomb_image, (bomb["x"] * TILE_SIZE, bomb["y"] * TILE_SIZE))

# Hàm vẽ vụ nổ
def draw_explosions():
    for explosion in explosions:
        screen.blit(explosion_image, (explosion["x"] * TILE_SIZE, explosion["y"] * TILE_SIZE))

# Hàm xử lý vụ nổ
def trigger_explosion(bomb):
    x, y = bomb["x"], bomb["y"]
    explosion_positions = [
        {"x": x, "y": y},
        {"x": x + 1, "y": y},
        {"x": x - 1, "y": y},
        {"x": x, "y": y + 1},
        {"x": x, "y": y - 1},
    ]
    return explosion_positions

# Vòng lặp chính
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(BLACK)
    draw_grid()
    draw_player()
    draw_bombs()
    draw_explosions()

    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and player["x"] > 0:
                player["x"] -= 1
            if event.key == pygame.K_RIGHT and player["x"] < COLS - 1:
                player["x"] += 1
            if event.key == pygame.K_UP and player["y"] > 0:
                player["y"] -= 1
            if event.key == pygame.K_DOWN and player["y"] < ROWS - 1:
                player["y"] += 1
            if event.key == pygame.K_SPACE:
                # Đặt bom tại vị trí của nhân vật
                bombs.append({"x": player["x"], "y": player["y"], "timer": time.time()})

    # Xử lý bom
    current_time = time.time()
    for bomb in bombs[:]:
        if current_time - bomb["timer"] > 2:  # Bom nổ sau 2 giây
            explosions.extend(trigger_explosion(bomb))
            bombs.remove(bomb)

    # Xóa vụ nổ sau 1 giây
    for explosion in explosions[:]:
        if current_time - bomb["timer"] > 3:  # Xóa vụ nổ sau 1 giây
            explosions.remove(explosion)

    pygame.display.flip()
    clock.tick(10)
