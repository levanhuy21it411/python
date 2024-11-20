# Nhập vào một số nguyên dương
n = int(input("Nhập vào một số nguyên dương n: "))

# Kiểm tra xem n có phải là số dạng 2^k không
while n > 1:
    if n % 2 != 0:
        print(f"{n} không phải là số dạng 2^k.")
        break
    n = n // 2
else:
    if n == 1:
        print(f"{n} là số dạng 2^k.")
    else:
        print(f"{n} không phải là số dạng 2^k.")
