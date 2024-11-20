n = int(input("Nhập vào số nguyên n: "))
tong_nguyen_to = 0
so_nguyen_to = 0

print("Các số nguyên tố từ 1 đến", n, "là:", end=" ")

for i in range(2, n + 1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i, end=" ")
        tong_nguyen_to += i
        so_nguyen_to += 1
print("\nTổng các số nguyên tố từ 1 đến", n, "là:", tong_nguyen_to)
print("Có", so_nguyen_to, "số nguyên tố trong khoảng từ 1 đến", n)
