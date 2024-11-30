n=int(input("Nhập n: "))
def giaithua(n):
    tich=1
    for i in range(1,n+1):
        tich*=i
    return tich
print("n!= ",giaithua(n))