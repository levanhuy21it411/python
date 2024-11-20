import pygame
import sys
import random

# Khởi tạo pygame
pygame.init()

# Kích thước màn hình
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Khủng Long Nhảy")

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Tốc độ
clock = pygame.time.Clock()
FPS = 60

# Font chữ
font = pygame.font.Font(None, 36)

# Khủng long
dino_width, dino_height = 50, 50
dino_x, dino_y = 50, HEIGHT - dino_height - 20
dino_vel_y = 0
gravity = 1.2
is_jumping = False

# Chướng ngại vật
obstacle_width, obstacle_height = 20, 40
obstacle_x = WIDTH
obstacle_y = HEIGHT - obstacle_height - 20

# Tốc độ trò chơi
base_speed = 5
speed = base_speed

# Điểm số
score = 0

# Vẽ khủng long
def draw_dino(x, y):
    pygame.draw.rect(screen, BLACK, (x, y, dino_width, dino_height))

# Vẽ chướng ngại vật
def draw_obstacle(x, y):
    pygame.draw.rect(screen, BLACK, (x, y, obstacle_width, obstacle_height))

# Vẽ điểm số
def draw_score(score):
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

# Hiển thị thông báo thua
def draw_game_over():
    game_over_text = font.render("Game Over! Nhấn R để chơi lại.", True, BLACK)
    screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2))

# Reset trò chơi
def reset_game():
    global dino_y, dino_vel_y, is_jumping, obstacle_x, speed, score
    dino_y = HEIGHT - dino_height - 20
    dino_vel_y = 0
    is_jumping = False
    obstacle_x = WIDTH
    speed = base_speed
    score = 0

# Hàm chính
def main():
    global dino_y, dino_vel_y, is_jumping, obstacle_x, speed, score
    running = True
    game_over = False

    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not is_jumping and not game_over:
                    dino_vel_y = -15
                    is_jumping = True
                if event.key == pygame.K_r and game_over:
                    reset_game()
                    game_over = False

        # Cập nhật vị trí khủng long
        dino_y += dino_vel_y
        if is_jumping:
            dino_vel_y += gravity
        if dino_y >= HEIGHT - dino_height - 20:
            dino_y = HEIGHT - dino_height - 20
            is_jumping = False

        # Di chuyển chướng ngại vật
        if not game_over:
            obstacle_x -= speed
            if obstacle_x < -obstacle_width:
                obstacle_x = WIDTH
                score += 1
                speed += 0.5  # Tăng tốc độ khi vượt qua mỗi chướng ngại vật

        # Va chạm
        if (
            obstacle_x < dino_x + dino_width
            and obstacle_x + obstacle_width > dino_x
            and obstacle_y < dino_y + dino_height
        ):
            game_over = True

        # Vẽ khủng long và chướng ngại vật
        draw_dino(dino_x, dino_y)
        draw_obstacle(obstacle_x, obstacle_y)

        # Vẽ điểm số
        draw_score(score)

        # Vẽ thông báo thua nếu cần
        if game_over:
            draw_game_over()

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
