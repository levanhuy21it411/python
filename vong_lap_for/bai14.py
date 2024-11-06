n=int(input("nhập một số nguyên "))
if n>=10:
    for x in range(10,n+1):
        # hàm range(10, n+1) chạy các số nguyên từ 10 đến n
        print(x,end=" ")
else:
    print("nhập số phải lớn hơn 10")