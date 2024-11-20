import pygame
import sys
import random

# Khởi tạo Pygame
pygame.init()

# Kích thước màn hình
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Survival Shooting Game")

# Màu sắc
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Tạo người chơi
player_size = 50
player = pygame.Rect(width // 2, height - player_size - 10, player_size, player_size)
player_speed = 5
player_health = 100

# Danh sách đạn
bullets = []
bullet_speed = 10

# Tạo kẻ địch
enemy_size = 40
enemies = []
enemy_speed = 2
spawn_delay = 30  # Khoảng thời gian để tạo kẻ địch mới
enemy_timer = 0

# Vòng lặp game chính
clock = pygame.time.Clock()
while True:
    screen.fill(white)  # Làm mới màn hình với màu trắng

    # Kiểm tra sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Bắn đạn khi nhấn phím SPACE
                bullet = pygame.Rect(player.centerx, player.centery, 5, 10)  # Đạn bắn lên trên
                bullets.append(bullet)

    # Điều khiển người chơi
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.right < width:
        player.x += player_speed
    if keys[pygame.K_UP] and player.top > 0:
        player.y -= player_speed
    if keys[pygame.K_DOWN] and player.bottom < height:
        player.y += player_speed

    # Cập nhật đạn di chuyển lên trên
    for bullet in bullets[:]:
        bullet.y -= bullet_speed  # Di chuyển đạn lên trên
        if bullet.y < 0:  # Xóa đạn khi ra khỏi màn hình
            bullets.remove(bullet)

    # Sinh kẻ địch mới theo thời gian
    enemy_timer += 1
    if enemy_timer >= spawn_delay:
        enemy_x = random.randint(0, width - enemy_size)
        enemy_y = random.randint(-100, -40)  # Để kẻ địch sinh ra từ trên cao
        enemy = pygame.Rect(enemy_x, enemy_y, enemy_size, enemy_size)
        enemies.append(enemy)
        enemy_timer = 0

    # Cập nhật vị trí kẻ địch và kiểm tra va chạm với người chơi
    for enemy in enemies[:]:
        enemy.y += enemy_speed
        if enemy.colliderect(player):  # Kẻ địch va chạm với người chơi
            player_health -= 10  # Giảm máu của người chơi
            enemies.remove(enemy)
        elif enemy.top > height:  # Xóa kẻ địch nếu ra khỏi màn hình
            enemies.remove(enemy)

    # Kiểm tra va chạm giữa đạn và kẻ địch
    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
                break
    
    # Vẽ người chơi
    player_image = pygame.image.load('D:/python/gane/image/MPSS_Mario.png')
    player_image = pygame.transform.scale(player_image, (30, 30))  # Chỉnh kích thước về 30x30

    screen.blit(player_image, player)

    # Vẽ đạn
    font = pygame.font.Font(None, 36)  # Font mặc định, kích thước 36

    for bullet in bullets:
        text_surface = font.render("Ngu", True, red)
        screen.blit(text_surface, (bullet.x, bullet.y))

    # Vẽ kẻ địch
    # Tải và lật ảnh kẻ địch
    enemy_image = pygame.image.load('D:/python/gane/image/chaubao.png')
    enemy_image = pygame.transform.scale(enemy_image, (40, 40))
    enemy_image = pygame.transform.flip(enemy_image, True, False)  # Lật ngang nếu cần

    # Vẽ ảnh kẻ địch
    for enemy in enemies:
        screen.blit(enemy_image, (enemy.x, enemy.y))


    # Vẽ thanh máu
    pygame.draw.rect(screen, red, (10, 10, player_health * 2, 20))

    # Cập nhật màn hình và tốc độ khung hình
    pygame.display.update()
    clock.tick(60)

    # Kiểm tra kết thúc trò chơi
    if player_health <= 0:
        print("Game Over!")
        pygame.quit()
        sys.exit()
 