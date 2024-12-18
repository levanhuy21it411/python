n=int(input("Nhap kích thước danh sách"))
list=[]
def nhap(list,n):
    for i in range(n):
        print("Nhập phần tử thứ",i)
        list.append(int(input()))
    return list
def gia_tri_tang(list,n):
    for i in range(0,n):
        for j in range(i,n):
            if list[i]>list[j]:
                t=list[i]
                list[i]=list[j]
                list[j]=t
    return list
print(f"Chương trình có mảng trước sắp xếp là: {nhap(list,n)}")
print(f"Chương trình có mảng sau sắp xếp là: {gia_tri_tang(list,n)}")