# Nhập danh sách số nguyên từ người dùng
L = list(map(int, input("Nhập các số nguyên, cách nhau bởi khoảng trắng: ").split()))

# Tìm giá trị lớn nhất
max_value = max(L)

# In ra giá trị lớn nhất
print("Giá trị lớn nhất trong danh sách là:", max_value)
