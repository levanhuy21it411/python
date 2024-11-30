a=int(input("Nhập a: "))
b=int(input("Nhập b: "))
c=int(input("Nhập c: "))
def kiemtra(a,b,c):
     if a >= b and a >= c:
        return a
     elif b >= a and b >= c:
        return b
     else:
        return c
print("kiểm tra số lớn nhất là",kiemtra(a,b,c))