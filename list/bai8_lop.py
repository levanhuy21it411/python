n=int(input("Nhap kích thước danh sách"))

list=[]
def nhap(list,n):
    for i in range(n):
        print("Nhập phần tử thứ",i)
        list.append(int(input()))
    return list
def kiem_tra(list,n):
    ktra=0
    for i in list:
        if x==i:
           ktra=1
    return ktra
print(f"Mảng vừa nhập là: {nhap(list,n)}")
x=int(input("Nhập vào x: "))
if kiem_tra(list,n)==1:
    print(f"{x} có trong mảng")
else:
    print(f"{x} không có trong mảng")
    list.insert(0,x)
    print(list)
