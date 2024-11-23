n=int(input("Nhập số nguyên N: "))
s=0
p=1
while n>0:
    du=n%10
    s=s+du
    p=p*du
    n=n//10
print(s)
print(p)