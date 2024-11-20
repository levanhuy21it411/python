# Nhập vào chuỗi từ người dùng
text = input("Nhập vào một chuỗi: ")

# Khởi tạo các biến đếm
upper_count = 0
lower_count = 0
digit_count = 0

# Duyệt qua từng ký tự trong chuỗi
for char in text:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1
    elif char.isdigit():
        digit_count += 1

# In kết quả
print("Số ký tự in hoa:", upper_count)
print("Số ký tự in thường:", lower_count)
print("Số ký tự số:", digit_count)
