n=int(input("Nhap kích thước danh sách"))
list=[]
def nhap(list,n):
    for i in range(n):
        print("Nhập phần tử thứ",i)
        list.append(int(input()))
    return list
def gia_tri_nho(list,n):
    min=list[0]
    for i in list:
        if i<min:
            min=i
    print("Giá trị nhỏ nhất trong mảng là",min)
print(nhap(list,n))
gia_tri_nho(list,n)