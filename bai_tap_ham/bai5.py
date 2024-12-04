n=int(input("Nhập số nguyên n: "))
def tong_chu_so(n):
    tong=0
    while n > 0:
        a = n % 10
        n //= 10
        tong+=a
    return tong
def tich_chu_so(n):
    tich=1
    while n > 0:
        a = n % 10
        n //= 10
        tich*=a
    return tich
print("Tổng các chữ số trong số nguyên",n,"là :",tong_chu_so(n))
print("Tích các chữ số trong số nguyên",n,"là :",tich_chu_so(n))