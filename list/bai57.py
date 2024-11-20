L=list(map(int,input("Nhập vào một chuỗi L: ").split()))
gtam =0
for i in L:
    if i<0:
        if gtam==0 or gtam<i:
            gtam=i
print(gtam)