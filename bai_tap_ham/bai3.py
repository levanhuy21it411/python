import math
a=int(input("Nhập số nguyên a: "))
b=int(input("Nhập số nguyên b: "))
c=int(input("Nhập số nguyên c: "))
def phuong_trinh_bac_1(a,b):
    if a==0 and b==0:
        return str("Phương trình vô số nghiệm")
    if a==0 and b!=0:
        return str("Phương trình vô nghiệm")
    if a!=0:
        x=-b/a
        return x
def phuong_trinh_bac_2(a,b,c):
    deta=b**2-4-a*c
    if deta<0:
        return str("Phương trình vô nghiệm")
    if deta==0:
        x1=x2=(-b)/2*a
        print("Phương trình có nghiệm kép: x1 , x2 =",x1)
    if deta>0:
        x1=(-b+math.sqrt(deta))/2*a
        x2=(-b-math.sqrt(deta))/2*a
        print("Phương trình có hai nghiệm: x1 =",x1,"x2 =",x2)
if a==0:
   print( phuong_trinh_bac_1(a,b))
if a!=0:
    print("Kết quả chương trình là:",phuong_trinh_bac_2(a,b,c))