a=int(input("Nhập số nguyên a: "))
b=int(input("Nhập số nguyên b: "))
def phuong_trinh_bac_1(a,b):
    if a==0 and b==0:
        return str("Phương trình vô số nghiệm")
    if a==0 and b!=0:
        return str("Phương trình vô nghiệm")
    if a!=0:
        x=-b/a
        return x
print("Đáp án của phương trình: ",a,"* x +",b,"=",phuong_trinh_bac_1(a,b))