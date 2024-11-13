# Nhập số đầu tiên và khởi tạo giá trị lớn nhất và nhỏ nhất
number = int(input("Nhập số nguyên (nhập -1 để kết thúc): "))
max_number = number
min_number = number
    # Sử dụng vòng lặp while với điều kiện   
while number != -1:
        number = int(input("Nhập số nguyên (nhập -1 để kết thúc): "))
        if number == -1:
            break
        # Cập nhật giá trị lớn nhất và nhỏ nhất
        if number > max_number:
            max_number = number
        if number < min_number:
            min_number = number
    # In kết quả
print("Số lớn nhất:", max_number)
print("Số nhỏ nhất:", min_number)
