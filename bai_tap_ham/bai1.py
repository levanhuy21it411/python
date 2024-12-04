n=int(input("Nhập số nguyên n: "))
def tong_chan(n):
    sum=0
    for i in range(1,n+1):
        if i%2==0:
            sum+=i
    return sum
print("Tổng các số nguyên từ 1 đến",n,"là: ",tong_chan(n))