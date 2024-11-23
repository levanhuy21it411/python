import pygame
import sys

# Khởi tạo pygame
pygame.init()

# Kích thước màn hình
WIDTH, HEIGHT = 800, 600
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Two Player Fighting Game")

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Tốc độ khung hình
FPS = 60
fpsClock = pygame.time.Clock()

# Thông tin người chơi
player1 = pygame.Rect(100, 500, 50, 50)  # Vị trí và kích thước người chơi 1
player2 = pygame.Rect(650, 500, 50, 50)  # Vị trí và kích thước người chơi 2

player1_health = 100
player2_health = 100

player1_mana = 100
player2_mana = 100

player1_speed = 5
player2_speed = 5

special1 = None
special2 = None

# Phím di chuyển
player1_controls = {"left": pygame.K_a, "right": pygame.K_d, "attack": pygame.K_w, "special": pygame.K_s}
player2_controls = {"left": pygame.K_LEFT, "right": pygame.K_RIGHT, "attack": pygame.K_UP, "special": pygame.K_DOWN}

# Hình chữ nhật tấn công
attack1 = pygame.Rect(0, 0, 40, 40)  # Để mô phỏng đòn đánh của người chơi 1
attack2 = pygame.Rect(0, 0, 40, 40)  # Để mô phỏng đòn đánh của người chơi 2

# Trạng thái tấn công
player1_attacking = False
player2_attacking = False

attack_duration = 10
player1_attack_timer = 0
player2_attack_timer = 0

# Phông chữ
font = pygame.font.Font(None, 36)

def draw_health():
    pygame.draw.rect(DISPLAYSURF, RED, (50, 50, player1_health * 2, 20))
    pygame.draw.rect(DISPLAYSURF, RED, (WIDTH - 250, 50, player2_health * 2, 20))

    p1_text = font.render("P1 Health", True, WHITE)
    p2_text = font.render("P2 Health", True, WHITE)

    DISPLAYSURF.blit(p1_text, (50, 20))
    DISPLAYSURF.blit(p2_text, (WIDTH - 250, 20))

def draw_mana():
    pygame.draw.rect(DISPLAYSURF, BLUE, (50, 80, player1_mana * 2, 20))
    pygame.draw.rect(DISPLAYSURF, BLUE, (WIDTH - 250, 80, player2_mana * 2, 20))

    p1_text = font.render("P1 Mana", True, WHITE)
    p2_text = font.render("P2 Mana", True, WHITE)

    DISPLAYSURF.blit(p1_text, (50, 60))
    DISPLAYSURF.blit(p2_text, (WIDTH - 250, 60))

def check_collision():
    global player1_health, player2_health

    if player1_attacking and attack1.colliderect(player2):
        player2_health -= 10
    if player2_attacking and attack2.colliderect(player1):
        player1_health -= 10

def check_special_collision(special, target):
    if special and special.colliderect(target):
        return True
    return False

def game_loop():
    global player1_health, player2_health  # Thêm khai báo global
    global player1_attacking, player2_attacking, player1_attack_timer, player2_attack_timer
    global player1_mana, player2_mana, special1, special2

    running = True
    while running:
        DISPLAYSURF.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        # Điều khiển người chơi 1
        if keys[player1_controls["left"]]:
            player1.x -= player1_speed
        if keys[player1_controls["right"]]:
            player1.x += player1_speed
        if keys[player1_controls["attack"]] and not player1_attacking:
            player1_attacking = True
            player1_attack_timer = attack_duration
            attack1.x = player1.x + player1.width
            attack1.y = player1.y
        if keys[player1_controls["special"]] and player1_mana >= 50 and special1 is None:
            player1_mana -= 50
            special1 = pygame.Rect(player1.x + player1.width, player1.y, 20, 20)

        # Điều khiển người chơi 2
        if keys[player2_controls["left"]]:
            player2.x -= player2_speed
        if keys[player2_controls["right"]]:
            player2.x += player2_speed
        if keys[player2_controls["attack"]] and not player2_attacking:
            player2_attacking = True
            player2_attack_timer = attack_duration
            attack2.x = player2.x - attack2.width
            attack2.y = player2.y
        if keys[player2_controls["special"]] and player2_mana >= 50 and special2 is None:
            player2_mana -= 50
            special2 = pygame.Rect(player2.x - 20, player2.y, 20, 20)

        # Vẽ người chơi
        pygame.draw.rect(DISPLAYSURF, BLUE, player1)
        pygame.draw.rect(DISPLAYSURF, GREEN, player2)

        # Vẽ tấn công
        if player1_attacking:
            pygame.draw.rect(DISPLAYSURF, WHITE, attack1)
            player1_attack_timer -= 1
            if player1_attack_timer <= 0:
                player1_attacking = False

        if player2_attacking:
            pygame.draw.rect(DISPLAYSURF, WHITE, attack2)
            player2_attack_timer -= 1
            if player2_attack_timer <= 0:
                player2_attacking = False

        # Vẽ chiêu đặc biệt
        if special1:
            pygame.draw.rect(DISPLAYSURF, RED, special1)
            special1.x += 10
            if special1.x > WIDTH or check_special_collision(special1, player2):
                if check_special_collision(special1, player2):
                    player2_health -= 20
                special1 = None

        if special2:
            pygame.draw.rect(DISPLAYSURF, RED, special2)
            special2.x -= 10
            if special2.x < 0 or check_special_collision(special2, player1):
                if check_special_collision(special2, player1):
                    player1_health -= 20
                special2 = None

        # Kiểm tra va chạm
        check_collision()

        # Vẽ máu và năng lượng
        draw_health()
        draw_mana()

        # Kiểm tra kết thúc
        if player1_health <= 0 or player2_health <= 0:
            winner_text = "Player 1 Wins!" if player2_health <= 0 else "Player 2 Wins!"
            text = font.render(winner_text, True, WHITE)
            DISPLAYSURF.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))
            pygame.display.update()
            pygame.time.wait(3000)
            return

        pygame.display.update()
        fpsClock.tick(FPS)

# Chạy game
game_loop()
