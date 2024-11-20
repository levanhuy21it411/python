L= list(map(int,input("Nhap vao chuoi so nguyen L: ").split()))
a=int(input("Nhap vao so nguyen a: "))
b=int(input("Nhap vao so nguyen b: "))
if a < b< len(L):
    sublist= L[a:b+1]
    min=min(sublist)
    print("Số nhỏ nhất trong đoạn từ vị trí", a, "đến", b, "là:", min)
else:
     print("Điều kiện a < b < len(L) không hợp lệ!")