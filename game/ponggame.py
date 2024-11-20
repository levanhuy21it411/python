import pygame
import sys

# Khởi tạo Pygame
pygame.init()

# Cài đặt màn hình
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Cài đặt thanh và bóng
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 20

player1 = pygame.Rect(50, (HEIGHT // 2) - (PADDLE_HEIGHT // 2), PADDLE_WIDTH, PADDLE_HEIGHT)
player2 = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, (HEIGHT // 2) - (PADDLE_HEIGHT // 2), PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

# Tốc độ
PADDLE_SPEED = 30
BALL_SPEED_X, BALL_SPEED_Y = 6, 6

# Điểm
score1, score2 = 0, 0
font = pygame.font.Font(None, 36)

# Hàm hiển thị điểm
def draw_score():
    score_text = font.render(f"{score1} - {score2}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))

# Vòng lặp game
clock = pygame.time.Clock()

while True:
    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Điều khiển thanh
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1.top > 0:
        player1.y -= PADDLE_SPEED
    if keys[pygame.K_s] and player1.bottom < HEIGHT:
        player1.y += PADDLE_SPEED
    if keys[pygame.K_UP] and player2.top > 0:
        player2.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and player2.bottom < HEIGHT:
        player2.y += PADDLE_SPEED

    # Di chuyển bóng
    ball.x += BALL_SPEED_X
    ball.y += BALL_SPEED_Y

    # Va chạm với tường
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        BALL_SPEED_Y *= -1

    # Va chạm với thanh
    if ball.colliderect(player1) or ball.colliderect(player2):
        BALL_SPEED_X *= -1

    # Ghi điểm
    if ball.left <= 0:
        score2 += 1
        ball.x, ball.y = WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2
        BALL_SPEED_X *= -1
    if ball.right >= WIDTH:
        score1 += 1
        ball.x, ball.y = WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2
        BALL_SPEED_X *= -1

    # Vẽ màn hình
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player1)
    pygame.draw.rect(screen, WHITE, player2)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    draw_score()

    pygame.display.flip()
    clock.tick(60)
