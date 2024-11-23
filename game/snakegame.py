import pygame
import random

# Khởi tạo pygame
pygame.init()

# Kích thước cửa sổ
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Rắn Săn Mồi")

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Kích thước mỗi ô
SNAKE_SIZE = 10

# Khởi tạo rắn
snake_body = [(100, 50), (90, 50), (80, 50)]  # Vị trí ban đầu của rắn
snake_direction = 'RIGHT'  # Hướng di chuyển ban đầu
food_position = (random.randrange(1, (WIDTH // SNAKE_SIZE)) * SNAKE_SIZE,
                 random.randrange(1, (HEIGHT // SNAKE_SIZE)) * SNAKE_SIZE)  # Vị trí ban đầu của thức ăn
food_spawn = True
score = 0

# Tốc độ game
clock = pygame.time.Clock()

# Hàm vẽ màn hình
def draw():
    screen.fill(BLACK)

    # Vẽ rắn
    for segment in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))

    # Vẽ thức ăn
    pygame.draw.rect(screen, RED, pygame.Rect(food_position[0], food_position[1], SNAKE_SIZE, SNAKE_SIZE))

    # Hiển thị điểm số
    font = pygame.font.SysFont(None, 35)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, [0, 0])

    pygame.display.flip()

# Hàm di chuyển rắn
def move_snake(direction, snake_body):
    head_x, head_y = snake_body[0]

    if direction == 'UP':
        head_y -= SNAKE_SIZE
    elif direction == 'DOWN':
        head_y += SNAKE_SIZE
    elif direction == 'LEFT':
        head_x -= SNAKE_SIZE
    elif direction == 'RIGHT':
        head_x += SNAKE_SIZE

    # Thêm đầu mới vào danh sách rắn
    new_head = (head_x, head_y)
    snake_body.insert(0, new_head)

    # Xóa phần cuối của rắn
    snake_body.pop()

# Kiểm tra va chạm
def check_collision(snake_body, food_position):
    global food_spawn, score

    head_x, head_y = snake_body[0]
    food_x, food_y = food_position

    # Nếu rắn ăn thức ăn
    if head_x == food_x and head_y == food_y:
        food_spawn = False
        score += 1
        snake_body.append(snake_body[-1])  # Tăng thêm một khúc rắn

    # Nếu rắn chạm vào tường hoặc chính nó
    if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
        return True
    if (head_x, head_y) in snake_body[1:]:
        return True

    return False

# Hàm chính
def main():
    global snake_direction, food_position, food_spawn, score, snake_body

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Điều khiển hướng di chuyển
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_direction != 'DOWN':
                    snake_direction = 'UP'
                elif event.key == pygame.K_DOWN and snake_direction != 'UP':
                    snake_direction = 'DOWN'
                elif event.key == pygame.K_LEFT and snake_direction != 'RIGHT':
                    snake_direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and snake_direction != 'LEFT':
                    snake_direction = 'RIGHT'

        # Di chuyển rắn
        move_snake(snake_direction, snake_body)

        # Kiểm tra va chạm
        if check_collision(snake_body, food_position):
            break  # Kết thúc game nếu va chạm

        # Tạo thức ăn mới nếu cần
        if not food_spawn:
            food_position = (random.randrange(1, (WIDTH // SNAKE_SIZE)) * SNAKE_SIZE,
                             random.randrange(1, (HEIGHT // SNAKE_SIZE)) * SNAKE_SIZE)
            food_spawn = True

        # Vẽ lại màn hình
        draw()

        # Điều chỉnh tốc độ game
        clock.tick(15 + score)  # Tăng tốc độ theo điểm số

    # Kết thúc game
    font = pygame.font.SysFont(None, 55)
    game_over_text = font.render(f"Game Over! Score: {score}", True, WHITE)
    screen.blit(game_over_text, [WIDTH // 4, HEIGHT // 2])
    pygame.display.flip()
    pygame.time.delay(2000)  # Hiển thị kết quả sau 2 giây

    pygame.quit()

if __name__ == "__main__":
    main()
