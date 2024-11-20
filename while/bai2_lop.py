x=1
n=int(input("Nhập vào số nguyên n: "))
print("Những số chẵn nhỏ hơn n")
while x<n:
    if x%2==0:
        print(x,end=" ")
    x+=1