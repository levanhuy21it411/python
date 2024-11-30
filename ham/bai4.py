n=int(input("Nhập n: "))
def tong(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    return sum
print("Tổng từ 1 đến n: ",tong(n))