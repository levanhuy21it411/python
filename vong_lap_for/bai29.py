a =int(input("Nhập số a: "))
print("Ước của a là :")
for i in range(1,a+1):
    if a%i==0:
        print(i,end=" ")