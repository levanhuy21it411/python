m=int(input("Nhập m"))
s=0
for i in range(1,m+1):
    for j in range(1,11):
        s+=i*j
print(s)