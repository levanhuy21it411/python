# Nhập chuỗi từ người dùng
chuoi = input("Nhập chuỗi: ")

tong = 0
i = 0
so = ""  # Chuỗi tạm thời để chứa các ký tự số liên tiếp

# Duyệt qua từng ký tự trong chuỗi bằng vòng lặp while
while i < len(chuoi):
    # Kiểm tra nếu ký tự hiện tại là số mà không dùng isdigit()
    if '0' <= chuoi[i] <= '9':
        so += chuoi[i]  # Ghép ký tự số vào chuỗi tạm thời
    else:
        # Nếu chuỗi so không rỗng, chuyển thành số nguyên và cộng vào tổng
        if so:
            tong += int(so)
            so = ""  # Đặt lại chuỗi tạm thời cho số mới

    i += 1  # Tiếp tục với ký tự tiếp theo

# Kiểm tra nếu còn số nào sót lại sau khi kết thúc vòng lặp
if so:
    tong += int(so)

print("Tổng:", tong)
