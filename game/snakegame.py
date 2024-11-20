import pygame
import random
import time

# Khởi tạo Pygame
pygame.init()

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)
YELLOW = (255, 255, 102)

# Kích thước cửa sổ
WIDTH = 800
HEIGHT = 600
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

# Các tham số của rắn
snake_block = 20
snake_speed = 15

# Font
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Biến toàn cục
player_name = ""
difficulty = "Easy"  # Độ khó mặc định
high_score = 0  # Điểm cao nhất

# Các hàm phụ trợ
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, BLACK)
    DISPLAYSURF.blit(value, [WIDTH - 200, 10])  # Hiển thị điểm ở góc phải trên cùng

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    DISPLAYSURF.blit(mesg, [WIDTH / 6, HEIGHT / 3])

def our_snake(snake_block, snake_List):
    for x in snake_List:
        pygame.draw.rect(DISPLAYSURF, GREEN, [x[0], x[1], snake_block, snake_block])

def spawn_food():
    x = round(random.randrange(0, WIDTH - snake_block) / 20.0) * 20.0
    y = round(random.randrange(0, HEIGHT - snake_block) / 20.0) * 20.0
    return x, y

def spawn_obstacle():
    x = round(random.randrange(0, WIDTH - snake_block) / 20.0) * 20.0
    y = round(random.randrange(0, HEIGHT - snake_block) / 20.0) * 20.0
    return x, y

# Hàm game loop chính
def game_loop():
    global snake_speed, player_name, high_score

    game_over = False
    game_close = False
    x1 = WIDTH / 2
    y1 = HEIGHT / 2
    x1_change = 0
    y1_change = 0

    # Khởi tạo rắn với 3 ô
    snake_List = []
    snake_List.append([x1, y1])
    snake_List.append([x1 - snake_block, y1])
    snake_List.append([x1 - 2 * snake_block, y1])
    Length_of_snake = 3

    food_position = spawn_food()
    obstacles = [spawn_obstacle() for _ in range(3)]  # Tạo 3 chướng ngại vật

    while not game_over:
        while game_close:
            DISPLAYSURF.fill(BLUE)
            message("You Lost! Press C-Play Again or Q-Quit", RED)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            # Tạo các nút "Play Again" và "High Score" khi game kết thúc
            create_button(200, 400, 200, 50, "Play Again", GREEN, RED, game_loop)
            create_button(200, 500, 200, 50, "High Score", GREEN, RED, show_high_score)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:  # Thoát game
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:  # Chơi lại
                        game_loop()

        # Xử lý các sự kiện
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Kiểm tra va chạm với tường
        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        DISPLAYSURF.fill(BLUE)
        pygame.draw.rect(DISPLAYSURF, YELLOW, [food_position[0], food_position[1], snake_block, snake_block])

        # Vẽ chướng ngại vật
        for obstacle in obstacles:
            pygame.draw.rect(DISPLAYSURF, RED, [obstacle[0], obstacle[1], snake_block, snake_block])

        # Di chuyển rắn
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Kiểm tra va chạm với chính mình
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        # Hiển thị tên người chơi và điểm hiện tại
        player_name_text = font_style.render(f"Player: {player_name}", True, BLACK)
        score_text = font_style.render(f"Score: {Length_of_snake - 1}", True, BLACK)
        DISPLAYSURF.blit(player_name_text, [10, 10])
        DISPLAYSURF.blit(score_text, [10, 40])

        pygame.display.update()

        # Kiểm tra nếu rắn ăn được đồ ăn
        if x1 == food_position[0] and y1 == food_position[1]:
            food_position = spawn_food()
            Length_of_snake += 1

        # Kiểm tra nếu rắn va chạm với chướng ngại vật
        for obstacle in obstacles:
            if x1 == obstacle[0] and y1 == obstacle[1]:
                game_close = True

        pygame.time.Clock().tick(snake_speed)

        # Cập nhật điểm cao nhất
        if Length_of_snake - 1 > high_score:
            high_score = Length_of_snake - 1

    pygame.quit()
    quit()

# Hàm để xem điểm cao nhất
def show_high_score():
    global high_score
    DISPLAYSURF.fill(BLUE)
    message(f"High Score: {high_score}", GREEN)
    pygame.display.update()
    time.sleep(3)
    start_screen()

# Hàm để nhập tên người chơi và bắt đầu game
def enter_name():
    global player_name
    input_active = True
    player_name = ""
    text = font_style.render("Enter your name: ", True, BLACK)
    input_box = pygame.Rect(WIDTH / 4, HEIGHT / 3, 200, 50)
    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_active = False  # Kết thúc nhập tên khi nhấn Enter
                    create_start_button()  # Hiển thị nút "Start Game"
                elif event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]
                else:
                    player_name += event.unicode

        DISPLAYSURF.fill(BLUE)
        pygame.draw.rect(DISPLAYSURF, WHITE, input_box)
        txt_surface = font_style.render(player_name, True, BLACK)
        DISPLAYSURF.blit(text, (WIDTH / 4, HEIGHT / 3 - 30))
        DISPLAYSURF.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.display.update()

# Hàm tạo nút "Start Game"
def create_start_button():
    create_button(WIDTH / 2, HEIGHT / 3, 200, 50, "Start Game", GREEN, RED, game_loop)
    create_button(WIDTH / 2, HEIGHT / 3 + 60, 200, 50, "High Score", GREEN, RED, show_high_score)

# Hàm tạo nút bằng chuột
def create_button(x, y, width, height, text, color, hover_color, function):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    pygame.draw.rect(DISPLAYSURF, color, (x, y, width, height))

    if x + width > mouse_x > x and y + height > mouse_y > y:
        pygame.draw.rect(DISPLAYSURF, hover_color, (x, y, width, height))
        if click[0] == 1:
            function()

    text_surface = font_style.render(text, True, BLACK)
    DISPLAYSURF.blit(text_surface, (x + width / 6, y + height / 6))

# Hàm màn hình bắt đầu
def start_screen():
    DISPLAYSURF.fill(BLUE)
    message("Snake Game", GREEN)
    pygame.display.update()

# Chạy chương trình
enter_name()
start_screen()
