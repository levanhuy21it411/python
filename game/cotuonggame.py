import pygame
import sys

# Khởi tạo Pygame
pygame.init()

# Kích thước màn hình
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cờ Tướng")

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Kích thước bàn cờ và ô cờ
ROWS, COLS = 10, 9
CELL_SIZE = WIDTH // COLS

# Bàn cờ
def draw_board():
    screen.fill(WHITE)
    for row in range(ROWS):
        for col in range(COLS):
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, BLACK, rect, 1)

    # Vẽ các đường thẳng giữa
    pygame.draw.line(screen, BLACK, (CELL_SIZE * 3, 0), (CELL_SIZE * 3, CELL_SIZE * 4), 2)
    pygame.draw.line(screen, BLACK, (CELL_SIZE * 5, 0), (CELL_SIZE * 5, CELL_SIZE * 4), 2)
    pygame.draw.line(screen, BLACK, (CELL_SIZE * 3, HEIGHT), (CELL_SIZE * 3, HEIGHT - CELL_SIZE * 4), 2)
    pygame.draw.line(screen, BLACK, (CELL_SIZE * 5, HEIGHT), (CELL_SIZE * 5, HEIGHT - CELL_SIZE * 4), 2)

# Quân cờ (mô phỏng cơ bản)
pieces = {
    "red_general": pygame.image.load('D:/python/gane/image/chaubao.png'),  # Thay bằng đường dẫn ảnh quân cờ
    "black_general": pygame.image.load('D:/python/gane/image/MPSS_Mario.png'),
}

# Vị trí quân cờ ban đầu
initial_positions = {
    "red_general": (4, 9),
    "black_general": (4, 0),
}

def draw_pieces():
    for piece, (col, row) in initial_positions.items():
        x = col * CELL_SIZE + CELL_SIZE // 2
        y = row * CELL_SIZE + CELL_SIZE // 2
        piece_image = pygame.transform.scale(pieces[piece], (CELL_SIZE - 10, CELL_SIZE - 10))
        screen.blit(piece_image, (x - piece_image.get_width() // 2, y - piece_image.get_height() // 2))

# Hàm chính
def main():
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        draw_board()
        draw_pieces()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
