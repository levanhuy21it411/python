import pygame
import sys
import math

# Khởi tạo Pygame
pygame.init()

# Cài đặt màn hình và màu sắc
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 15, 15
CELL_SIZE = WIDTH // COLS

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Khởi tạo màn hình
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cờ Caro - Tối ưu")

# Bàn cờ
board = [["" for _ in range(COLS)] for _ in range(ROWS)]

# Font chữ
font = pygame.font.Font(None, 72)

# Vẽ bàn cờ
def draw_board():
    screen.fill(WHITE)
    for row in range(ROWS):
        for col in range(COLS):
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, BLACK, rect, 1)

# Vẽ X và O
def draw_marks():
    for row in range(ROWS):
        for col in range(COLS):
            mark = board[row][col]
            x = col * CELL_SIZE + CELL_SIZE // 2
            y = row * CELL_SIZE + CELL_SIZE // 2
            if mark == "X":
                pygame.draw.line(screen, RED, (x - 20, y - 20), (x + 20, y + 20), 3)
                pygame.draw.line(screen, RED, (x + 20, y - 20), (x - 20, y + 20), 3)
            elif mark == "O":
                pygame.draw.circle(screen, BLUE, (x, y), 20, 3)

# Kiểm tra chiến thắng
def check_winner():
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] != "":
                # Kiểm tra hàng ngang
                if col <= COLS - 5 and all(board[row][col + i] == board[row][col] for i in range(5)):
                    return board[row][col]
                # Kiểm tra hàng dọc
                if row <= ROWS - 5 and all(board[row + i][col] == board[row][col] for i in range(5)):
                    return board[row][col]
                # Kiểm tra đường chéo xuống
                if row <= ROWS - 5 and col <= COLS - 5 and all(board[row + i][col + i] == board[row][col] for i in range(5)):
                    return board[row][col]
                # Kiểm tra đường chéo lên
                if row >= 4 and col <= COLS - 5 and all(board[row - i][col + i] == board[row][col] for i in range(5)):
                    return board[row][col]
    return None

# Hàm Minimax với Alpha-Beta Pruning
def minimax(is_maximizing, depth, alpha, beta):
    winner = check_winner()
    if winner == "O":  # Máy thắng
        return 10 - depth
    elif winner == "X":  # Người chơi thắng
        return depth - 10
    elif all(board[row][col] != "" for row in range(ROWS) for col in range(COLS)):  # Hòa
        return 0

    if depth >= 3:  # Giới hạn độ sâu để tăng tốc
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "":
                    board[row][col] = "O"
                    eval = minimax(False, depth + 1, alpha, beta)
                    board[row][col] = ""
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "":
                    board[row][col] = "X"
                    eval = minimax(True, depth + 1, alpha, beta)
                    board[row][col] = ""
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Bot chọn nước đi tốt nhất
def bot_move():
    best_score = -math.inf
    best_move = None
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == "":
                board[row][col] = "O"
                score = minimax(False, 0, -math.inf, math.inf)
                board[row][col] = ""
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    return best_move

# Vẽ thông báo chiến thắng
def draw_winner(winner):
    text = font.render(f"{winner} Wins!", True, RED if winner == "X" else BLUE)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

# Reset bàn cờ
def reset_board():
    global board
    board = [["" for _ in range(COLS)] for _ in range(ROWS)]

# Hàm chính
def main():
    clock = pygame.time.Clock()
    running = True
    current_player = "X"  # Người chơi bắt đầu
    winner = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and winner is None and current_player == "X":
                x, y = event.pos
                col = x // CELL_SIZE
                row = y // CELL_SIZE
                if board[row][col] == "":
                    board[row][col] = "X"
                    winner = check_winner()
                    current_player = "O"

        # Máy chơi (Bot)
        if current_player == "O" and winner is None:
            pygame.time.delay(300)  # Giảm độ trễ bot
            move = bot_move()
            if move:
                row, col = move
                board[row][col] = "O"
                winner = check_winner()
                current_player = "X"

        # Chơi lại khi kết thúc
        if winner and event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            reset_board()
            winner = None
            current_player = "X"

        draw_board()
        draw_marks()
        if winner:
            draw_winner(winner)

        pygame.display.flip()
        clock.tick(240)

if __name__ == "__main__":
    main()
