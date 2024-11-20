L=list(map(int,input("Nhập vào list số nguyên L: ").split()))
kt= True
for i in L:
    if i !=L[0]:
        kt= False
        break
if kt:
    print("Các phần tử bằng nhau")
else:
    print("Không có các phần tử bằng nhau")