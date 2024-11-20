L=list(map(int,input("Nhập vào chuỗi L: ").split()))
x=int(input("Nhập vào số nguyên x"))
kq=None
for i in L:
    if kq==None or abs(kq-x)<abs(i-x):
        kq=i
print(kq)