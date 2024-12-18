n=int(input("Nhap kích thước danh sách"))

list=[]
def nhap(list,n):
    for i in range(n):
        print("Nhập phần tử thứ",i)
        list.append(int(input()))
    return list
print(f"Mảng vừa nhập là: {nhap(list,n)}")
