import pygame
import os
import sys

# Khởi tạo pygame
pygame.init()

# Kích thước cửa sổ
WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ứng Dụng Nghe Nhạc")

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BUTTON_COLOR = (100, 150, 200)

# Đường dẫn file nhạc
music_file = "D:/python/game/music/test.mp3"  # Đường dẫn đến file nhạc

# Kiểm tra xem file nhạc có tồn tại không
if not os.path.exists(music_file):
    print(f"File nhạc '{music_file}' không tồn tại. Vui lòng kiểm tra lại đường dẫn.")
    sys.exit()  # Dừng chương trình nếu không tìm thấy file

# Chạy nhạc
def play_music():
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play(-1)  # Lặp lại nhạc vô hạn

# Dừng nhạc
def stop_music():
    pygame.mixer.music.stop()

# Tạm dừng/tiếp tục nhạc
def toggle_music():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()

# Giao diện ứng dụng
def draw_interface():
    screen.fill(WHITE)

    # Hiển thị tên bài hát
    font = pygame.font.Font(None, 36)
    song_name_text = font.render(os.path.basename(music_file), True, BLACK)
    screen.blit(song_name_text, (WIDTH // 2 - song_name_text.get_width() // 2, 30))

    # Các nút điều khiển
    play_button = pygame.Rect(WIDTH // 2 - 40, HEIGHT // 2 - 20, 80, 40)
    pygame.draw.rect(screen, BUTTON_COLOR, play_button)
    play_text = font.render("Play/Pause", True, WHITE)
    screen.blit(play_text, (WIDTH // 2 - play_text.get_width() // 2, HEIGHT // 2 - 20))

    pygame.display.flip()

# Hàm chính
def main():
    play_music()  # Bắt đầu phát nhạc khi mở ứng dụng
    running = True
    while running:
        draw_interface()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                # Kiểm tra nút Play/Pause
                if pygame.Rect(WIDTH // 2 - 40, HEIGHT // 2 - 20, 80, 40).collidepoint(mouse_pos):
                    toggle_music()

        pygame.display.update()

if __name__ == "__main__":
    main()
