# Nhập vào chuỗi từ người dùng
text = input("Nhập vào một chuỗi gồm 3 số nguyên, cách nhau bởi dấu phẩy: ")

# Tách chuỗi thành danh sách các số, loại bỏ khoảng trắng nếu có
numbers = text.split(',')

# Chuyển các số từ chuỗi sang số nguyên và tính tổng
total = int(numbers[0].strip()) + int(numbers[1].strip()) + int(numbers[2].strip())

print("Tổng của 3 số là:", total)
